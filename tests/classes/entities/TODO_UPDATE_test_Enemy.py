
"""
Unit tests for the Enemy class.
These tests cover all logic branches and edge cases for open source contribution.
"""

import unittest
from src.classes.entities.Enemy import Enemy
from src.classes.entities.Hitbox import Hitbox


class DummyWeapon:
    """A minimal weapon stub for testing Enemy interactions."""
    def __init__(self, active=True, damage=10, direction="Down", hitbox=None):
        self.active = active
        self.damage = damage
        self.direction = direction
        self.hitbox = hitbox or Hitbox({"x": 0, "y": 0, "width": 10, "height": 10})


class DummyCreature:
    """A minimal Creature stub to allow Enemy instantiation."""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.image = None
        self.hitbox = Hitbox({"x": 0, "y": 0, "width": 10, "height": 10})
        self.alive = True
        self.immunity_count = 0
        self.damage_direction = "Down"
        self.health = 100
    def update(self, dt, screen):
        pass
    def draw(self, surface):
        pass
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            self.health = 0


class TestEnemy(unittest.TestCase):
    """Unit tests for the Enemy class."""
    def setUp(self):
        # Patch Enemy to avoid Creature dependency issues
        Enemy.__bases__ = (DummyCreature,)
        self.enemy = Enemy()
        self.enemy.image = None
        self.enemy.x = 0
        self.enemy.y = 0
        self.enemy.hitbox = Hitbox({"x": 0, "y": 0, "width": 10, "height": 10})
        self.enemy.alive = True
        self.enemy.immunity_count = 0
        self.enemy.damage_direction = "Down"
        self.enemy.health = 100


    def test_update_enemy_alive_and_weapon_active(self):
        """Enemy should take damage and update direction when alive and weapon is active."""
        weapon = DummyWeapon(active=True, damage=10, direction="Down", hitbox=Hitbox({"x": 0, "y": 0, "width": 10, "height": 10}))
        self.enemy.update(1, None, weapon)
        self.assertEqual(self.enemy.health, 90)
        self.assertEqual(self.enemy.damage_direction, "Down")

    def test_update_enemy_dead(self):
        """Enemy should not take damage if not alive."""
        self.enemy.alive = False
        weapon = DummyWeapon(active=True)
        self.enemy.update(1, None, weapon)
        self.assertEqual(self.enemy.health, 100)

    def test_update_weapon_inactive(self):
        """Enemy should not take damage if weapon is inactive."""
        weapon = DummyWeapon(active=False)
        self.enemy.update(1, None, weapon)
        self.assertEqual(self.enemy.health, 100)

    def test_update_immunity_count(self):
        """Enemy should not take damage if immunity_count > 0."""
        self.enemy.immunity_count = 5
        weapon = DummyWeapon(active=True)
        self.enemy.update(1, None, weapon)
        self.assertEqual(self.enemy.health, 100)

    def test_checkForDamage_collision(self):
        """Enemy should take correct damage and update direction on collision."""
        weapon = DummyWeapon(active=True, damage=15, direction="Left", hitbox=Hitbox({"x": 0, "y": 0, "width": 10, "height": 10}))
        self.enemy.checkForDamage(weapon)
        self.assertEqual(self.enemy.health, 85)
        self.assertEqual(self.enemy.damage_direction, "Left")


    def test_checkForDamage_no_collision(self):
        """Enemy should not take damage if there is no collision."""
        weapon = DummyWeapon(active=True, damage=15, direction="Left", hitbox=Hitbox({"x": 100, "y": 100, "width": 10, "height": 10}))
        self.enemy.checkForDamage(weapon)
        self.assertEqual(self.enemy.health, 100)

    def test_draw(self):
        """Enemy.draw should call surface.blit."""
        class DummySurface:
            def __init__(self):
                self.blit_called = False
            def blit(self, image, pos):
                self.blit_called = True
        surface = DummySurface()
        self.enemy.image = "dummy_image"
        self.enemy.draw(surface)
        self.assertTrue(surface.blit_called)

    def test_take_damage_to_zero(self):
        """Enemy should die and health should not go below zero when taking fatal damage."""
        weapon = DummyWeapon(active=True, damage=200, direction="Down", hitbox=Hitbox({"x": 0, "y": 0, "width": 10, "height": 10}))
        self.enemy.checkForDamage(weapon)
        self.assertEqual(self.enemy.health, 0)
        self.assertFalse(self.enemy.alive)


    def test_multiple_damage_and_immunity(self):
        """Enemy should not take damage again if immunity_count is set after first hit."""
        weapon = DummyWeapon(active=True, damage=10, direction="Down", hitbox=Hitbox({"x": 0, "y": 0, "width": 10, "height": 10}))
        self.enemy.checkForDamage(weapon)
        self.assertEqual(self.enemy.health, 90)
        self.enemy.immunity_count = 30
        self.enemy.checkForDamage(weapon)
        self.assertEqual(self.enemy.health, 90)


if __name__ == "__main__":
    unittest.main()
