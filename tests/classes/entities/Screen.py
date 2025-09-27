"""
Unit tests for the Screen class.
These tests cover all logic branches and edge cases for open source contribution.
"""

import unittest
import pygame
from unittest.mock import Mock, MagicMock, patch
from classes.entities.Screen import Screen

class TestScreen(unittest.TestCase):

    def setUp(self):
        # Create mock tiles
        self.mock_tile1 = Mock()
        self.mock_tile2 = Mock()
        self.mock_tile3 = Mock()
        self.mock_tile4 = Mock()
        
        # Create mock creatures
        self.mock_creature1 = Mock()
        self.mock_creature1.alive = True
        self.mock_creature2 = Mock()
        self.mock_creature2.alive = True
        
        # Set up basic screen parameters
        self.width = 800
        self.height = 600
        self.tiles_wide = 2
        self.tiles_high = 2
        self.tiles = [self.mock_tile1, self.mock_tile2, self.mock_tile3, self.mock_tile4]
        self.creatures = [self.mock_creature1, self.mock_creature2]
        
        # Create the screen instance
        self.screen = Screen(
            self.width, 
            self.height, 
            self.tiles_wide, 
            self.tiles_high, 
            self.tiles, 
            self.creatures
        )

    def test_init(self):
        self.assertEqual(self.screen.width, 800)
        self.assertEqual(self.screen.height, 600)
        self.assertEqual(self.screen.tiles_wide, 2)
        self.assertEqual(self.screen.tiles_high, 2)
        # Test calculated properties
        self.assertEqual(self.screen.tile_width, 400)  # 800 // 2
        self.assertEqual(self.screen.tile_height, 300)  # 600 // 2
        self.assertEqual(self.screen.tiles, self.tiles)
        self.assertEqual(self.screen.creatures, self.creatures)
        self.assertFalse(self.screen.active)  # Should default to False

    def test_width_property(self):
        # Test getter
        self.assertEqual(self.screen.width, 800)
        
        # Test setter
        self.screen.width = 1000
        self.assertEqual(self.screen.width, 1000)

    def test_height_property(self):
        # Test getter
        self.assertEqual(self.screen.height, 600)
        
        # Test setter
        self.screen.height = 800
        self.assertEqual(self.screen.height, 800)

    def test_tiles_wide_property(self):
        # Test getter
        self.assertEqual(self.screen.tiles_wide, 2)
        
        # Test setter
        self.screen.tiles_wide = 4
        self.assertEqual(self.screen.tiles_wide, 4)

    def test_tiles_high_property(self):
        # Test getter
        self.assertEqual(self.screen.tiles_high, 2)
        
        # Test setter
        self.screen.tiles_high = 3
        self.assertEqual(self.screen.tiles_high, 3)

    def test_tile_width_property(self):
        # Test getter
        self.assertEqual(self.screen.tile_width, 400)
        
        # Test setter
        self.screen.tile_width = 200
        self.assertEqual(self.screen.tile_width, 200)

    def test_tile_height_property(self):
        # Test getter
        self.assertEqual(self.screen.tile_height, 300)
        
        # Test setter
        self.screen.tile_height = 150
        self.assertEqual(self.screen.tile_height, 150)

    def test_tiles_property(self):
        # Test getter
        self.assertEqual(self.screen.tiles, self.tiles)
        
        # Test setter
        new_tiles = [Mock(), Mock()]
        self.screen.tiles = new_tiles
        self.assertEqual(self.screen.tiles, new_tiles)

    def test_active_property(self):
        # Test getter (should default to False)
        self.assertFalse(self.screen.active)
        
        # Test setter
        self.screen.active = True
        self.assertTrue(self.screen.active)

    def test_creatures_property(self):
        # Test getter
        self.assertEqual(self.screen.creatures, self.creatures)
        
        # Test setter
        new_creatures = [Mock(), Mock(), Mock()]
        self.screen.creatures = new_creatures
        self.assertEqual(self.screen.creatures, new_creatures)

    def test_update_with_normal_creatures(self):
        dt = 0.016
        world_map = Mock()
        weapon = Mock()
        
        # Call update
        self.screen.update(dt, world_map, weapon)
        
        # Verify both creatures were updated with all three parameters
        self.mock_creature1.update.assert_called_once_with(dt, world_map, weapon)
        self.mock_creature2.update.assert_called_once_with(dt, world_map, weapon)

    def test_update_with_simple_creatures(self):
        dt = 0.016
        world_map = Mock()
        weapon = Mock()
        
        # Make creatures raise TypeError for 3-parameter call
        self.mock_creature1.update.side_effect = [TypeError(), None]
        self.mock_creature2.update.side_effect = [TypeError(), None]
        
        # Call update
        self.screen.update(dt, world_map, weapon)
        
        # Verify creatures were called first with 3 params, then with 2 params
        expected_calls_creature1 = [
            unittest.mock.call(dt, world_map, weapon),
            unittest.mock.call(dt, world_map)
        ]
        expected_calls_creature2 = [
            unittest.mock.call(dt, world_map, weapon),
            unittest.mock.call(dt, world_map)
        ]
        
        self.assertEqual(self.mock_creature1.update.call_args_list, expected_calls_creature1)
        self.assertEqual(self.mock_creature2.update.call_args_list, expected_calls_creature2)

    def test_update_with_dead_creatures(self):
        dt = 0.016
        world_map = Mock()
        weapon = Mock()
        
        # Make one creature dead
        self.mock_creature1.alive = False
        self.mock_creature2.alive = True
        
        # Call update
        self.screen.update(dt, world_map, weapon)
        
        # Verify only the alive creature was updated
        self.mock_creature1.update.assert_not_called()
        self.mock_creature2.update.assert_called_once_with(dt, world_map, weapon)

    def test_update_with_empty_creatures_list(self):
        screen = Screen(800, 600, 2, 2, self.tiles, [])
        dt = 0.016
        world_map = Mock()
        weapon = Mock()
        
        # Should not raise any exceptions
        screen.update(dt, world_map, weapon)

    def test_draw_method(self):
        surface = Mock()
        
        # Call draw
        self.screen.draw(surface)
        
        # Verify all tiles had their background drawn
        self.mock_tile1.draw_background.assert_called_once_with(self.screen, surface, 0, 0)
        self.mock_tile2.draw_background.assert_called_once_with(self.screen, surface, 400, 0)
        self.mock_tile3.draw_background.assert_called_once_with(self.screen, surface, 0, 300)
        self.mock_tile4.draw_background.assert_called_once_with(self.screen, surface, 400, 300)
        
        # Verify all tiles had their foreground drawn
        self.mock_tile1.draw_foreground.assert_called_once_with(self.screen, surface, 0, 0)
        self.mock_tile2.draw_foreground.assert_called_once_with(self.screen, surface, 400, 0)
        self.mock_tile3.draw_foreground.assert_called_once_with(self.screen, surface, 0, 300)
        self.mock_tile4.draw_foreground.assert_called_once_with(self.screen, surface, 400, 300)
        
        # Verify all alive creatures were drawn
        self.mock_creature1.draw.assert_called_once_with(surface)
        self.mock_creature2.draw.assert_called_once_with(surface)

    def test_draw_with_dead_creatures(self):
        surface = Mock()
        
        # Make one creature dead
        self.mock_creature1.alive = False
        self.mock_creature2.alive = True
        
        # Call draw
        self.screen.draw(surface)
        
        # Verify only alive creature was drawn
        self.mock_creature1.draw.assert_not_called()
        self.mock_creature2.draw.assert_called_once_with(surface)

    def test_draw_with_args_and_kwargs(self):
        surface = Mock()
        extra_arg = "test"
        extra_kwarg = {"test": "value"}
        
        # Call draw with additional arguments
        self.screen.draw(surface, extra_arg, **extra_kwarg)
        
        # Verify creatures received the extra arguments
        self.mock_creature1.draw.assert_called_once_with(surface, extra_arg, **extra_kwarg)
        self.mock_creature2.draw.assert_called_once_with(surface, extra_arg, **extra_kwarg)

    def test_init_with_zero_tiles_wide(self):
        # This would cause division by zero in tile_width calculation
        with self.assertRaises(ZeroDivisionError):
            Screen(800, 600, 0, 2, self.tiles, self.creatures)

    def test_init_with_zero_tiles_high(self):
        # This would cause division by zero in tile_height calculation
        with self.assertRaises(ZeroDivisionError):
            Screen(800, 600, 2, 0, self.tiles, self.creatures)

    def test_init_with_negative_dimensions(self):
        # Should still work, just creates negative tile sizes
        screen = Screen(-800, -600, 2, 2, self.tiles, self.creatures)
        self.assertEqual(screen.width, -800)
        self.assertEqual(screen.height, -600)
        self.assertEqual(screen.tile_width, -400)
        self.assertEqual(screen.tile_height, -300)

    def test_init_with_empty_tiles_list(self):
        screen = Screen(800, 600, 2, 2, [], self.creatures)
        self.assertEqual(screen.tiles, [])

    def test_init_with_none_values(self):
        screen = Screen(800, 600, 2, 2, None, None)
        self.assertIsNone(screen.tiles)
        self.assertIsNone(screen.creatures)

    def test_draw_with_insufficient_tiles(self):
        # Create screen that expects 4 tiles but only provide 2
        insufficient_tiles = [self.mock_tile1, self.mock_tile2]
        screen = Screen(800, 600, 2, 2, insufficient_tiles, self.creatures)
        surface = Mock()
        
        # Should not raise exception, should reuse last tile
        screen.draw(surface)
        
        # Verify the last tile gets reused
        self.assertEqual(self.mock_tile2.draw_background.call_count, 3)  # Called for positions 1, 2, and 3
        self.assertEqual(self.mock_tile2.draw_foreground.call_count, 3)  # Called for positions 1, 2, and 3

    def test_update_with_mixed_creature_types(self):
        dt = 0.016
        world_map = Mock()
        weapon = Mock()
        
        # First creature accepts 3 params, second only accepts 2
        self.mock_creature1.update.side_effect = None  # Works with 3 params
        self.mock_creature2.update.side_effect = [TypeError(), None]  # Fails then works with 2
        
        # Call update
        self.screen.update(dt, world_map, weapon)
        
        # Verify first creature only called once with 3 params
        self.mock_creature1.update.assert_called_once_with(dt, world_map, weapon)
        
        # Verify second creature called twice (3 params fail, then 2 params succeed)
        expected_calls = [
            unittest.mock.call(dt, world_map, weapon),
            unittest.mock.call(dt, world_map)
        ]
        self.assertEqual(self.mock_creature2.update.call_args_list, expected_calls)


if __name__ == "__main__":
    unittest.main()

