import random
from src.classes.entities.Creature import Creature
from src.classes.entities.Enemy import Enemy

class WanderingEnemy(Enemy):
  def __init__(
    self,
    animationSpeed,
    animations,
    width=100,
    height=100,
    x=0,
    y=0,
    hitbox_offset_dimentions={"x": 0, "y": 0, "width": 0, "height": 0},
    hitbox_visible=False,
    wander_speed=80,
    change_dir_min=0.8,
    change_dir_max=2.0,
    idle_chance=0.12,
    alive=True,
    health=100,
    display_health=True
  ):
    super().__init__(
      animationSpeed=animationSpeed,
      animations = animations,
      width=width,
      height=height,
      x=x,
      y=y,
      hitbox_offset_dimentions=hitbox_offset_dimentions,
      hitbox_visible=hitbox_visible,
      alive=alive,
      health=health,
      display_health=display_health
    )
    self._wander_speed = wander_speed
    self._change_dir_min = change_dir_min
    self._change_dir_max = change_dir_max
    self._idle_chance = idle_chance
    self._wander_time_left = random.uniform(self._change_dir_min, self._change_dir_max)
    self._wander_direction = random.choice(["Up", "Down", "Left", "Right"])
    self._current_animation = self.animations["Idle"]

  def _dir_multiplier(self, direction: str) -> float:
    if direction == "Up":
      return self.up_speed
    if direction == "Down":
      return self.down_speed
    if direction == "Left":
      return self.left_speed
    if direction == "Right":
      return self.right_speed
    return 1.0

  def _choose_new_direction(self):
    candidates = ["Up", "Down", "Left", "Right"]
    allowed = [d for d in candidates if self._dir_multiplier(d) > 0]
    if not allowed:
      allowed = candidates
    if random.random() < self._idle_chance:
      self._wander_direction = None
    else:
      self._wander_direction = random.choice(allowed)
    self._wander_time_left = random.uniform(self._change_dir_min, self._change_dir_max)

  def update(self, dt, FRAMERATE, world_map, weapon):
    # Collisions, immunity, animation
    Creature.update(self, dt, FRAMERATE, world_map)
    if not self.alive:
      return

    # Wandering AI
    self._wander_time_left -= dt
    if self._wander_time_left <= 0 or (
      self._wander_direction is not None and self._dir_multiplier(self._wander_direction) == 0
    ):
      self._choose_new_direction()

    if self._wander_direction is None:
      self.moving = False
    else:
      mult = self._dir_multiplier(self._wander_direction)
      effective_speed = self._wander_speed * mult
      if effective_speed > 0:
        self.moveDirection(dt, self._wander_direction, effective_speed)
      else:
        self.moving = False

    # Damage check
    if weapon.active and self.immunity_count <= 0:
      self.checkForDamage(weapon)
