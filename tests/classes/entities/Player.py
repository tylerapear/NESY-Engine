# tests/classes/entities/Player.py
import unittest
from unittest.mock import patch, MagicMock
import pygame

# Patch Animations BEFORE importing Player/Creature/Hitbox so no filesystem access
with patch("classes.effects.Animations.Animations") as MockAnimations:
    anim_instance = MagicMock()
    anim_instance.getNextImage = lambda creature, immunity: pygame.Surface((1, 1))
    MockAnimations.return_value = anim_instance

    # safe to import after patching
    from classes.entities.Player import Player
    from classes.entities.Hitbox import Hitbox

# --- helpers ---
class DummyItem:
    def __init__(self):
        self.updated_with = None
        self.drawn_on = None
        self.moved_with = None

    def update(self, player):
        self.updated_with = player

    def drawHitbox(self, surface):
        self.drawn_on = surface

    def moveHitbox(self, player):
        self.moved_with = player

class DummyWeapon:
    def __init__(self):
        self.active = False

class DummyScreen:
    def __init__(self, width=200, height=200, tiles=None):
        self.width = width
        self.height = height
        self.tiles = tiles or []

class DummyTile:
    def __init__(self, x, y, w, h, hitbox_active=True):
        self.hitbox_active = hitbox_active
        self.hitbox = Hitbox({"x": x, "y": y, "width": w, "height": h})

# --- Tests ---
class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()

        # create player (Animations is mocked)
        self.player = Player(
            spritePath="dummy_path",
            animationSpeed=5,
            width=50,
            height=50,
            x=10,
            y=10,
            hitbox_offset_dimentions={"x": 0, "y": 0, "width": 50, "height": 50},
            hitbox_visible=False,
            alive=True,
            health=100,
            display_health=False,
            inventory=[]
        )

        # ensure draw has an image
        self.player.image = pygame.Surface((50, 50))

        # inventory
        self.item = DummyItem()
        self.player.inventory = [self.item]

        # weapon
        self.weapon = DummyWeapon()

        # enemy overlapping player (real Hitbox)
        self.enemy = MagicMock()
        self.enemy.hitbox = Hitbox({"x": 10, "y": 10, "width": 50, "height": 50})
        self.enemy.alive = True

        # world map
        self.screenA = DummyScreen(width=300, height=200, tiles=[])
        self.world_map = MagicMock()
        self.world_map.current_screen = self.screenA
        self.world_map.setNextScreen = MagicMock(return_value=False)

        # surface
        self.surface = pygame.Surface((400, 400))

    # -----------------------
    # Properties
    # -----------------------
    def test_attacking_property_get_set(self):
        self.player.attacking = True
        self.assertTrue(self.player.attacking)
        self.player.attacking = False
        self.assertFalse(self.player.attacking)

    def test_attack_cooldown_property_get_set(self):
        self.player.attack_cooldown = 42
        self.assertEqual(self.player.attack_cooldown, 42)

    def test_inventory_property_get_set(self):
        inv = [DummyItem()]
        self.player.inventory = inv
        self.assertIs(self.player.inventory, inv)

    # -----------------------
    # attack()
    # -----------------------
    def test_attack_sets_cooldown_attacking_and_weapon_active(self):
        self.player.attack_cooldown = 0
        self.player.attack("Up", self.weapon)
        self.assertEqual(self.player.attack_cooldown, 15)
        self.assertTrue(self.player.attacking)
        self.assertTrue(self.weapon.active)
        self.assertEqual(self.player.current_animation, "AttackUp")

    def test_attack_does_nothing_if_cooldown_positive(self):
        self.player.attack_cooldown = 5
        self.weapon.active = False
        self.player.attack("Down", self.weapon)
        self.assertEqual(self.player.attack_cooldown, 5)
        self.assertFalse(self.weapon.active)

    # -----------------------
    # update() - attacking frame behavior
    # -----------------------
    def test_update_attacking_frame_count_resets_and_weapon_deactivated(self):
        self.player.attacking = True
        self.player.frame_count = 9  # next update increments to 10 -> reset
        self.weapon.active = True
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=[0] * 512):
            self.player.update(1, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(self.player.frame_count, 0)
        self.assertFalse(self.player.attacking)
        self.assertFalse(self.weapon.active)

    # -----------------------
    # update() - cooldown >0 branch where cooldown becomes <5
    # -----------------------
    def test_update_attack_cooldown_decrement_and_animation_reset_to_idle(self):
        self.player.attack_cooldown = 3
        self.player.attacking = True
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=[0] * 512):
            self.player.update(1, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(self.player.attack_cooldown, 2)
        self.assertFalse(self.player.attacking)
        # final assignment in update sets current_animation = "Idle" + direction
        self.assertEqual(self.player.current_animation, "Idle" + self.player.direction)

    # -----------------------
    # update() - cooldown >0 but still >=5 -> no animation reset to idle
    # -----------------------
    def test_update_cooldown_decrement_no_animation_reset_when_ge_5(self):
        self.player.attack_cooldown = 10
        self.player.attacking = True
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=[0] * 512):
            self.player.update(1, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(self.player.attack_cooldown, 9)
        # since still >=5, attacking remains True and final animation will be Attack + direction
        self.assertTrue(self.player.attacking)
        self.assertEqual(self.player.current_animation, "Attack" + self.player.direction)

    # -----------------------
    # update() - pressing attack key (K_j)
    # -----------------------
    def test_update_triggers_attack_on_keypress_j(self):
        keys = [0] * 512
        keys[pygame.K_j] = 1
        called = {}
        def fake_attack(direction, weapon):
            called['called'] = (direction, weapon)
        self.player.attack = fake_attack
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(1, self.world_map, self.surface, [], self.weapon)
        self.assertIn('called', called)
        self.assertEqual(called['called'][1], self.weapon)

    # -----------------------
    # update() - movement keys when not attacking (W, A, S, D)
    # -----------------------
    def test_update_handles_movement_keys_s_w_a_d(self):
        # test S (Down)
        keys = [0] * 512
        keys[pygame.K_s] = 1
        record = {}
        def fake_moveDirection(dt, direction, speed):
            record['s'] = direction
        self.player.attacking = False
        self.player.moveDirection = fake_moveDirection
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(0.25, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(record.get('s'), "Down")

        # test W (Up)
        keys = [0] * 512
        keys[pygame.K_w] = 1
        record = {}
        def fake_moveDirection2(dt, direction, speed):
            record['w'] = direction
        self.player.moveDirection = fake_moveDirection2
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(0.25, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(record.get('w'), "Up")

        # test A (Left)
        keys = [0] * 512
        keys[pygame.K_a] = 1
        record = {}
        def fake_moveDirection3(dt, direction, speed):
            record['a'] = direction
        self.player.moveDirection = fake_moveDirection3
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(0.25, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(record.get('a'), "Left")

        # test D (Right)
        keys = [0] * 512
        keys[pygame.K_d] = 1
        record = {}
        def fake_moveDirection4(dt, direction, speed):
            record['d'] = direction
        self.player.moveDirection = fake_moveDirection4
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(0.25, self.world_map, self.surface, [], self.weapon)
        self.assertEqual(record.get('d'), "Right")

    # -----------------------
    # update() - movement keys should be ignored when attacking
    # -----------------------
    def test_update_ignores_movement_keys_when_attacking(self):
        keys = [0] * 512
        keys[pygame.K_s] = 1
        called = {}
        def fake_moveDirection(dt, direction, speed):
            called['moved'] = True
        self.player.attacking = True
        self.player.moveDirection = fake_moveDirection
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=keys):
            self.player.update(0.1, self.world_map, self.surface, [], self.weapon)
        self.assertNotIn('moved', called)

    # -----------------------
    # inventory update called in update()
    # -----------------------
    def test_update_calls_inventory_update_for_each_item(self):
        item = DummyItem()
        self.player.inventory = [item]
        with patch("classes.entities.Player.pygame.key.get_pressed", return_value=[0] * 512):
            self.player.update(1, self.world_map, self.surface, [], self.weapon)
        self.assertIs(item.updated_with, self.player)

    # -----------------------
    # draw()
    # -----------------------
    def test_draw_blits_image_and_draws_inventory_hitboxes(self):
        self.player.draw(self.surface)
        # item.drawHitbox should be called with the surface
        self.assertIs(self.item.drawn_on, self.surface)

    # -----------------------
    # checkForDamage()
    # -----------------------
    def test_checkForDamage_applies_damage_and_immunity_and_sets_damage_direction(self):
        self.player.immunity_count = 0
        self.player.health = 50
        self.player.checkForDamage([self.enemy])
        self.assertEqual(self.player.immunity_count, 30)
        self.assertEqual(self.player.health, 40)
        self.assertIn(self.player.damage_direction, ("Up", "Down", "Left", "Right"))

    def test_checkForDamage_skips_dead_enemy(self):
        dead_enemy = MagicMock()
        dead_enemy.hitbox = Hitbox({"x": 10, "y": 10, "width": 50, "height": 50})
        dead_enemy.alive = False
        prev = self.player.health
        self.player.immunity_count = 0
        self.player.checkForDamage([dead_enemy])
        self.assertEqual(self.player.health, prev)

    def test_checkForDamage_kills_player_when_health_depletes(self):
        self.player.immunity_count = 0
        self.player.health = 5
        self.player.checkForDamage([self.enemy])
        self.assertFalse(self.player.alive)
        self.assertEqual(self.player.health, 0)

    def test_checkForDamage_ignores_when_immunity_positive(self):
        self.player.immunity_count = 5
        prev = self.player.health
        self.player.checkForDamage([self.enemy])
        self.assertEqual(self.player.health, prev)  # no change because immunity_count > 0

    # -----------------------
    # getKnockedBack / moveDirection inventory interaction
    # -----------------------
    def test_getKnockedBack_moves_inventory_hitboxes(self):
        item = DummyItem()
        self.player.inventory = [item]
        self.player.getKnockedBack(0.1, "Up", 100)
        self.assertIs(item.moved_with, self.player)

    def test_moveDirection_moves_inventory_hitboxes(self):
        item = DummyItem()
        self.player.inventory = [item]
        self.player.moveDirection(0.1, "Left", 10)
        self.assertIs(item.moved_with, self.player)

    # -----------------------
    # checkForGameOver
    # -----------------------
    def test_checkForGameOver_returns_true_when_dead(self):
        self.player.alive = False
        self.assertTrue(self.player.checkForGameOver())
        self.player.alive = True
        self.assertIsNone(self.player.checkForGameOver())

    # -----------------------
    # moveToNextScreen logic (setNextScreen True and False)
    # -----------------------
    def test_moveToNextScreen_up_down_left_right_when_setNextScreen_true(self):
        ws = MagicMock()
        screen = DummyScreen(width=320, height=240, tiles=[])
        ws.current_screen = screen
        ws.setNextScreen = MagicMock(return_value=True)

        # Up
        self.player.x = 15
        self.player.y = 20
        self.player.hitbox_offset_dimentions = {"x": 0, "y": 0, "width": 50, "height": 50}
        self.player.moveToNextScreen(ws, "Up")
        expected_y = screen.height - self.player.height + self.player.hitbox_offset_dimentions["y"] - 3
        self.assertEqual(self.player.y, expected_y)

        # Down
        self.player.x = 15
        self.player.y = 20
        self.player.moveToNextScreen(ws, "Down")
        expected_y = - self.player.hitbox_offset_dimentions["y"] - 3
        self.assertEqual(self.player.y, expected_y)

        # Left
        self.player.x = 15
        self.player.y = 20
        self.player.moveToNextScreen(ws, "Left")
        expected_x = screen.width - self.player.width + self.player.hitbox_offset_dimentions["x"] - 3
        self.assertEqual(self.player.x, expected_x)

        # Right
        self.player.x = 15
        self.player.y = 20
        self.player.moveToNextScreen(ws, "Right")
        expected_x = - self.player.hitbox_offset_dimentions["x"] - 3
        self.assertEqual(self.player.x, expected_x)

    def test_moveToNextScreen_calls_handleBorderCollision_when_setNextScreen_false(self):
        ws = MagicMock()
        ws.current_screen = DummyScreen(width=100, height=80)
        ws.setNextScreen = MagicMock(return_value=False)
        self.player.up_speed = 1
        self.player.moveToNextScreen(ws, "Up")
        self.assertEqual(self.player.up_speed, 0)

    # -----------------------
    # draw() with health display branch
    # -----------------------
    def test_draw_with_health_display_shows_text(self):
        self.player.display_health = True
        self.player.hitbox.visible = True
        # ensure draw doesn't raise
        self.player.draw(self.surface)

if __name__ == "__main__":
    unittest.main()
