"""
Unit tests for the Creature class.
These tests cover all logic branches and edge cases for open source contribution.
"""

import unittest
import pygame
from unittest.mock import Mock, MagicMock, patch
from classes.entities.Hitbox import Hitbox
from classes.entities.Creature import Creature



class TestHitbox(unittest.TestCase):
    """Unit tests for the Hitbox class"""

    def setUp(self):
        """Set up test fixtures"""

        self.hitbox = Hitbox(
            {"x":0, 
             "y":0, 
             "width":50, 
             "height":50},
             visible=False
        )

    def test_init(self):
        """Test hitbox initialization"""
        self.assertEqual(self.hitbox.x, 0)
        self.assertEqual(self.hitbox.y, 0)
        self.assertEqual(self.hitbox.width, 50)
        self.assertEqual(self.hitbox.height, 50)
        self.assertFalse(self.hitbox.visible)


    def test_property_setters_getters(self):
        """Test hitbox property setters and getters"""
        self.hitbox.x = 100
        self.assertEqual(self.hitbox.x, 100)

        self.hitbox.y = 100
        self.assertEqual(self.hitbox.y, 100)

        self.hitbox.width = 100
        self.assertEqual(self.hitbox.width, 100)

        self.hitbox.height = 100
        self.assertEqual(self.hitbox.height, 100)

        self.hitbox.visible = True
        self.assertTrue(self.hitbox.visible)


    @patch("pygame.draw.rect")
    def test_draw_visible_hitbox(self, mock):
        """Test draw method with visible hitbox"""
        surface = pygame.Surface((100, 100))
        self.hitbox.visible = True
        
        self.hitbox.draw(surface)

        mock.assert_called_once()
        args, kwargs = mock.call_args

        # First argument is surface
        self.assertEqual(args[0], surface)
        # Second argument is color
        self.assertEqual(args[1], (255, 0, 0))       
        # Third argument is hitbox dimensions
        self.assertEqual(args[2], (self.hitbox.x,
                                   self.hitbox.y,
                                   self.hitbox.height, 
                                   self.hitbox.width)) 
        # Fourth argument is visible boolean
        self.assertTrue(args[3])                  


    def test_handle_collision_true(self):
        """Test collision return True"""
        self.box2 = Hitbox({"x":0, "y":0, "width":50, "height":50}, visible=False)

        self.assertTrue(self.hitbox.collides(self.box2))

    def test_handle_collision_false(self):
        """Test collision return False"""
        self.box2 = Hitbox({"x":100, "y":100, "width":50, "height":50}, visible=False)

        self.assertFalse(self.hitbox.collides(self.box2))

    def test_collison_direction_down(self):
        """Test getCollisionDirection returns 'Down'"""
        self.box2 = Hitbox({"x":0, "y":-20, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getCollisionDirection(self.box2), "Down")

    def test_collison_direction_up(self):
        """Test getCollisionDirection returns 'Up'"""
        self.box2 = Hitbox({"x":0, "y":20, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getCollisionDirection(self.box2), "Up")

    def test_collison_direction_left(self):
        """Test getCollisionDirection returns 'Left'"""
        self.box2 = Hitbox({"x":20, "y":0, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getCollisionDirection(self.box2), "Left")

    def test_collison_direction_right(self):
        """Test getCollisionDirection returns 'Right'"""
        self.box2 = Hitbox({"x":-20, "y":10, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getCollisionDirection(self.box2), "Right")

    def test_reverse_collison_direction_down(self):
        """Test getReverseCollisionDirection returns 'Down'"""
        self.box2 = Hitbox({"x":0, "y":20, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getReverseCollisionDirection(self.box2), "Down")

    def test_reverse_collison_direction_up(self):
        """Test getReverseCollisionDirection returns 'Up'"""
        self.box2 = Hitbox({"x":0, "y":-20, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getReverseCollisionDirection(self.box2), "Up")

    def test_reverse_collison_direction_left(self):
        """Test getReverseCollisionDirection returns 'Left'"""
        self.box2 = Hitbox({"x":-20, "y":0, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getReverseCollisionDirection(self.box2), "Left")

    def test_reverse_collison_direction_right(self):
        """Test getReverseCollisionDirection returns 'Right'"""
        self.box2 = Hitbox({"x":20, "y":10, "width":50, "height":50}, visible=False)
        self.assertEqual(self.hitbox.getReverseCollisionDirection(self.box2), "Right")

if __name__ == "__main__":
    unittest.main()