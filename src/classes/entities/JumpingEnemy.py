import pygame
import random
from src.classes.entities.Enemy import Enemy

class JumpingEnemy(Enemy):
    def __init__(self, spritePath, animationSpeed, width=50, height=50, x=0, y=0,
                 hitbox_offset_dimentions={"x":0,"y":0,"width":0,"height":0},
                 hitbox_visible=False, alive=True, health=100, display_health=True):
        super().__init__(spritePath, animationSpeed, width, height, x, y,
                         hitbox_offset_dimentions, hitbox_visible, alive, health, display_health)
        self.jump_timer = 0
        self.pause_time = random.randint(60, 240)  # 60 fps → 1–4 seconds
        self.jumping = False

    def update(self, dt, screen, weapon):
        super().update(dt, screen, weapon)
        if not self.alive:
            return

        if self.jump_timer <= 0:
            if not self.jumping:
                self.jumping = True
                self.jump_direction = random.choice(["Up","Down","Left","Right"])
                self.jump_duration = random.randint(15,30)  # frames
            else:
                self.jumping = False
                self.pause_time = random.randint(60,240)

            self.jump_timer = self.jump_duration if self.jumping else self.pause_time

        if self.jumping:
            if self.jump_direction == "Up":
                self.moveDirection(dt, "Up", 150)
            elif self.jump_direction == "Down":
                self.moveDirection(dt, "Down", 150)
            elif self.jump_direction == "Left":
                self.moveDirection(dt, "Left", 150)
            elif self.jump_direction == "Right":
                self.moveDirection(dt, "Right", 150)

        self.jump_timer -= 1

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, (self.x, self.y))