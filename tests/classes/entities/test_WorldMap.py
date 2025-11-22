"""
Unit tests for the WorldMap class.
These tests cover all logic branches and edge cases for open source contribution.
"""
import unittest
import pygame
from unittest.mock import Mock, MagicMock, patch
from src.classes.entities.WorldMap import WorldMap

class TestWorldMap(unittest.TestCase):
    """Unit tests for the WorldMap class"""

    def setUp(self):
        """Set up test fixtures"""
        
        self.screens = [
            {"id": 0, "name": "Screen 0"},
            {"id": 1, "name": "Screen 1"},
            {"id": 2, "name": "Screen 2"},
            {"id": 3, "name": "Screen 3"}
        ]
        self.world_map = WorldMap(
            screens_wide=2,
            screens_high=2,
            screens=self.screens,
            start_screen_index=0
        )
    
    def test_init(self):
        """Test WorldMap initialization"""
        self.assertEqual(self.world_map.screens_wide, 2)
        self.assertEqual(self.world_map.screens_high, 2)
        self.assertEqual(self.world_map.screens, self.screens)
        self.assertEqual(self.world_map.start_screen_index, 0)
        self.assertEqual(self.world_map.current_screen, self.screens[0])

    def test_property_setters_getters(self):
        """Test WorldMap property setters and getters"""
        self.world_map.screens_wide = 3
        self.assertEqual(self.world_map.screens_wide, 3)

        self.world_map.screens_high = 3
        self.assertEqual(self.world_map.screens_high, 3)

        new_screens = [
            {"id": 0, "name": "New Screen 0"},
            {"id": 1, "name": "New Screen 1"}
        ]
        self.world_map.screens = new_screens
        self.assertEqual(self.world_map.screens, new_screens)

        self.world_map.start_screen_index = 1
        self.assertEqual(self.world_map.start_screen_index, 1)

        self.world_map.current_screen = new_screens[1]
        self.assertEqual(self.world_map.current_screen, new_screens[1])
    
    def test_invalid_start_index_raises(self):
        """Test WorldMap raises error with invalid start index"""
        with self.assertRaises(IndexError):
            WorldMap(2, 2, self.screens, start_screen_index=10)
    
    def test_empty_screens_list(self):
        """Test WorldMap with empty screens list"""
        with self.assertRaises(IndexError):
            WorldMap(2, 2, [], 0)

    def test_setNextScreen_valid_direction(self):
        """Test setNextScreen with valid direction"""
        next_screen = self.world_map.setNextScreen("Right")
        self.assertEqual(next_screen, self.screens[1])
        self.assertEqual(self.world_map.current_screen, self.screens[1])

        next_screen = self.world_map.setNextScreen("Down")
        self.assertEqual(next_screen, self.screens[3])
        self.assertEqual(self.world_map.current_screen, self.screens[3])

        next_screen = self.world_map.setNextScreen("Left")
        self.assertEqual(next_screen, self.screens[2])
        self.assertEqual(self.world_map.current_screen, self.screens[2])

        next_screen = self.world_map.setNextScreen("Up")
        self.assertEqual(next_screen, self.screens[0])
        self.assertEqual(self.world_map.current_screen, self.screens[0])
    
    def test_setNextScreen_invalid_direction(self):
        """Test setNextScreen with invalid direction"""
        self.world_map.current_screen = self.screens[0]
        next_screen = self.world_map.setNextScreen("Up")
        self.assertIsNone(next_screen)
        self.assertEqual(self.world_map.current_screen, self.screens[0])

        next_screen = self.world_map.setNextScreen("Left")
        self.assertIsNone(next_screen)
        self.assertEqual(self.world_map.current_screen, self.screens[0])

        self.world_map.current_screen = self.screens[1]
        next_screen = self.world_map.setNextScreen("Right")
        self.assertIsNone(next_screen)
        self.assertEqual(self.world_map.current_screen, self.screens[1])

        self.world_map.current_screen = self.screens[2]
        next_screen = self.world_map.setNextScreen("Down")
        self.assertIsNone(next_screen)
        self.assertEqual(self.world_map.current_screen, self.screens[2])
    
    def test_getScreenIfExists(self):
        """Test getScreenIfExists method"""
        screen = self.world_map.getScreenIfExists(1)
        self.assertEqual(screen, self.screens[1])

        screen = self.world_map.getScreenIfExists(4)
        self.assertIsNone(screen)
    
    def test_getNextScreen(self):
        """Test getNextScreen method"""
        self.world_map.current_screen = self.screens[0]

        next_screen = self.world_map.getNextScreen("Right")
        self.assertEqual(next_screen, self.screens[1])

        next_screen = self.world_map.getNextScreen("Up")
        self.assertIsNone(next_screen)

        self.world_map.current_screen = self.screens[1]
        next_screen = self.world_map.getNextScreen("Down")
        self.assertEqual(next_screen, self.screens[3])

        next_screen = self.world_map.getNextScreen("Right")
        self.assertIsNone(next_screen)

        self.world_map.current_screen = self.screens[2]
        next_screen = self.world_map.getNextScreen("Up")
        self.assertEqual(next_screen, self.screens[0])

        next_screen = self.world_map.getNextScreen("Left")
        self.assertIsNone(next_screen)

        self.world_map.current_screen = self.screens[3]
        next_screen = self.world_map.getNextScreen("Left")
        self.assertEqual(next_screen, self.screens[2])

        next_screen = self.world_map.getNextScreen("Down")
        self.assertIsNone(next_screen)

if __name__ == '__main__':
    unittest.main()