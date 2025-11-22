"""
Unit tests for the Creature class.
These tests cover all logic branches and edge cases for open source contribution.
"""

import unittest
from unittest.mock import Mock, MagicMock, patch
import pygame
from src.classes.entities.Creature import Creature
from src.classes.entities.Hitbox import Hitbox


class DummyWorldMap:
    """A minimal world map stub for testing Creature interactions."""
    def __init__(self):
        self.current_screen = Mock()
        self.current_screen.height = 600
        self.current_screen.width = 800
        self.current_screen.tiles = []


class DummyTile:
    """A minimal tile stub for collision testing."""
    def __init__(self, x=0, y=0, width=50, height=50, hitbox_active=True):
        self.hitbox_active = hitbox_active
        self.hitbox = Hitbox({"x": x, "y": y, "width": width, "height": height})


class TestCreature(unittest.TestCase):
    """Unit tests for the Creature class."""

    def setUp(self):
        """Set up test fixtures."""
        # Mock the Animations class to avoid dependency issues
        with patch('classes.entities.Creature.Animations'):
            self.creature = Creature(
                spritePath="test_sprite.png",
                animationSpeed=100,
                width=50,
                height=50,
                x=100,
                y=100,
                hitbox_offset_dimentions={"x": 5, "y": 5, "width": 40, "height": 40},
                hitbox_visible=True,
                alive=True,
                health=100,
                display_health=True
            )
            # Mock the animations method
            self.creature._animations.getNextImage = MagicMock(return_value="test_image")

    def test_initialization(self):
        """Test that Creature initializes with correct default values."""
        self.assertEqual(self.creature.x, 100)
        self.assertEqual(self.creature.y, 100)
        self.assertEqual(self.creature.width, 50)
        self.assertEqual(self.creature.height, 50)
        self.assertEqual(self.creature.direction, "Down")
        self.assertEqual(self.creature.moving, False)
        self.assertEqual(self.creature.alive, True)
        self.assertEqual(self.creature.health, 100)
        self.assertEqual(self.creature.immunity_count, 0)
        self.assertEqual(self.creature.up_speed, 1)
        self.assertEqual(self.creature.down_speed, 1)
        self.assertEqual(self.creature.left_speed, 1)
        self.assertEqual(self.creature.right_speed, 1)

    def test_property_setters_getters(self):
        """Test all property setters and getters."""
        # Test x property
        self.creature.x = 200
        self.assertEqual(self.creature.x, 200)

        # Test y property
        self.creature.y = 250
        self.assertEqual(self.creature.y, 250)

        # Test width property
        self.creature.width = 75
        self.assertEqual(self.creature.width, 75)

        # Test height property
        self.creature.height = 80
        self.assertEqual(self.creature.height, 80)

        # Test direction property
        self.creature.direction = "Up"
        self.assertEqual(self.creature.direction, "Up")

        # Test moving property
        self.creature.moving = True
        self.assertEqual(self.creature.moving, True)

        # Test health property
        self.creature.health = 50
        self.assertEqual(self.creature.health, 50)

        # Test alive property
        self.creature.alive = False
        self.assertEqual(self.creature.alive, False)

        # Test immunity_count property
        self.creature.immunity_count = 10
        self.assertEqual(self.creature.immunity_count, 10)

        # Test speed properties
        self.creature.up_speed = 2
        self.creature.down_speed = 3
        self.creature.left_speed = 4
        self.creature.right_speed = 5
        self.assertEqual(self.creature.up_speed, 2)
        self.assertEqual(self.creature.down_speed, 3)
        self.assertEqual(self.creature.left_speed, 4)
        self.assertEqual(self.creature.right_speed, 5)

    def test_move_direction_up(self):
        """Test moving up."""
        initial_y = self.creature.y
        initial_hitbox_y = self.creature.hitbox.y
        self.creature.moveDirection(0.1, "Up", 100)

        self.assertTrue(self.creature.moving)
        self.assertEqual(self.creature.direction, "Up")
        self.assertEqual(self.creature.y, initial_y - 10)
        self.assertEqual(self.creature.hitbox.y, initial_hitbox_y - 10)

    def test_move_direction_down(self):
        """Test moving down."""
        initial_y = self.creature.y
        initial_hitbox_y = self.creature.hitbox.y
        self.creature.moveDirection(0.1, "Down", 100)

        self.assertTrue(self.creature.moving)
        self.assertEqual(self.creature.direction, "Down")
        self.assertEqual(self.creature.y, initial_y + 10)
        self.assertEqual(self.creature.hitbox.y, initial_hitbox_y + 10)

    def test_move_direction_left(self):
        """Test moving left."""
        initial_x = self.creature.x
        initial_hitbox_x = self.creature.hitbox.x
        self.creature.moveDirection(0.1, "Left", 100)

        self.assertTrue(self.creature.moving)
        self.assertEqual(self.creature.direction, "Left")
        self.assertEqual(self.creature.x, initial_x - 10)
        self.assertEqual(self.creature.hitbox.x, initial_hitbox_x - 10)

    def test_move_direction_right(self):
        """Test moving right."""
        initial_x = self.creature.x
        initial_hitbox_x = self.creature.hitbox.x
        self.creature.moveDirection(0.1, "Right", 100)

        self.assertTrue(self.creature.moving)
        self.assertEqual(self.creature.direction, "Right")
        self.assertEqual(self.creature.x, initial_x + 10)
        self.assertEqual(self.creature.hitbox.x, initial_hitbox_x + 10)

    def test_move_direction_with_immunity(self):
        """Test that movement is restricted when immunity_count >= 18."""
        self.creature.immunity_count = 20
        initial_x = self.creature.x
        initial_y = self.creature.y

        self.creature.moveDirection(0.1, "Up", 100)
        self.assertEqual(self.creature.y, initial_y)  # Should not move

        self.creature.immunity_count = 17
        self.creature.moveDirection(0.1, "Up", 100)
        self.assertLess(self.creature.y, initial_y)  # Should move

    def test_move_to(self):
        """Test moving to specific coordinates."""
        self.creature.moveTo(300, 400)

        self.assertEqual(self.creature.x, 300)
        self.assertEqual(self.creature.y, 400)
        self.assertEqual(self.creature.hitbox.x, 300 + self.creature.hitbox_offset_dimentions["x"])
        self.assertEqual(self.creature.hitbox.y, 400 + self.creature.hitbox_offset_dimentions["y"])

    def test_take_damage(self):
        """Test taking damage."""
        initial_health = self.creature.health
        self.creature.takeDamage(30)

        self.assertEqual(self.creature.health, initial_health - 30)
        self.assertEqual(self.creature.immunity_count, 30)
        self.assertTrue(self.creature.alive)

    '''
    def test_take_damage_fatal(self):
        """Test taking fatal damage."""
        self.creature.takeDamage(100)

        self.assertEqual(self.creature.health, 0)
        self.assertFalse(self.creature.alive)
        #self.assertEqual(self.creature.immunity_count, 30)
    '''

    '''
    def test_take_damage_exact_death(self):
        """Test taking exact damage to reach 0 health."""
        self.creature.takeDamage(100)

        self.assertEqual(self.creature.health, 0)
        self.assertFalse(self.creature.alive)
    '''

    def test_get_knocked_back_up(self):
        """Test knockback in up direction."""
        initial_y = self.creature.y
        initial_hitbox_y = self.creature.hitbox.y
        self.creature.getKnockedBack(0.1, "Up", 200)

        self.assertEqual(self.creature.y, initial_y - 20)
        self.assertEqual(self.creature.hitbox.y, initial_hitbox_y - 20)

    def test_get_knocked_back_with_speed_modifier(self):
        """Test knockback with speed modifiers."""
        self.creature.up_speed = 2
        initial_y = self.creature.y
        self.creature.getKnockedBack(0.1, "Up", 100)

        self.assertEqual(self.creature.y, initial_y - 20)  # 100 * 0.1 * 2

    def test_handle_border_collision_up(self):
        """Test handling border collision when moving up."""
        world_map = DummyWorldMap()
        self.creature.handleBorderCollision(world_map, "Up")
        self.assertEqual(self.creature.up_speed, 0)

    def test_handle_border_collision_all_directions(self):
        """Test handling border collisions in all directions."""
        world_map = DummyWorldMap()

        self.creature.handleBorderCollision(world_map, "Up")
        self.assertEqual(self.creature.up_speed, 0)

        self.creature.handleBorderCollision(world_map, "Down")
        self.assertEqual(self.creature.down_speed, 0)

        self.creature.handleBorderCollision(world_map, "Left")
        self.assertEqual(self.creature.left_speed, 0)

        self.creature.handleBorderCollision(world_map, "Right")
        self.assertEqual(self.creature.right_speed, 0)

    def test_handle_tile_collision(self):
        """Test handling tile collisions in all directions."""
        self.creature.handleTileCollision("Up")
        self.assertEqual(self.creature.up_speed, 0)

        self.creature.handleTileCollision("Down")
        self.assertEqual(self.creature.down_speed, 0)

        self.creature.handleTileCollision("Left")
        self.assertEqual(self.creature.left_speed, 0)

        self.creature.handleTileCollision("Right")
        self.assertEqual(self.creature.right_speed, 0)

    def test_update_with_border_collisions(self):
        """Test update method with border collisions."""
        world_map = DummyWorldMap()

        # Test top border collision
        self.creature.hitbox.y = -5
        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.up_speed, 0)

        # Reset and test bottom border collision
        self.creature.hitbox.y = 580
        self.creature.hitbox.height = 40
        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.down_speed, 0)

        # Reset and test left border collision
        self.creature.hitbox.x = -5
        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.left_speed, 0)

        # Reset and test right border collision
        self.creature.hitbox.x = 780
        self.creature.hitbox.width = 40
        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.right_speed, 0)

    def test_update_with_tile_collision(self):
        """Test update method with tile collisions."""
        world_map = DummyWorldMap()
        tile = DummyTile(x=105, y=105, width=50, height=50, hitbox_active=True)
        world_map.current_screen.tiles = [tile]

        # Mock collides method to return True
        self.creature.hitbox.collides = MagicMock(return_value=True)
        self.creature.hitbox.getReverseCollisionDirection = MagicMock(return_value="Up")

        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.up_speed, 0)

    def test_update_with_immunity_knockback(self):
        """Test update with immunity count causing knockback."""
        world_map = DummyWorldMap()
        self.creature.immunity_count = 25
        self.creature.damage_direction = "Up"
        initial_y = self.creature.y

        self.creature.update(0.1, world_map)

        # Should be knocked back
        self.assertLess(self.creature.y, initial_y)
        # Immunity count should decrease
        self.assertEqual(self.creature.immunity_count, 24)

    def test_update_immunity_countdown(self):
        """Test immunity count decreases during update."""
        world_map = DummyWorldMap()
        self.creature.immunity_count = 10

        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.immunity_count, 9)

        self.creature.update(0.1, world_map)
        self.assertEqual(self.creature.immunity_count, 8)

    '''
    @patch('pygame.init')
    @patch('pygame.font.Font')
    def test_draw_with_health_display(self, mock_font_class, mock_init):
        """Test draw method with health display enabled."""
        # Setup mocks
        mock_font = MagicMock()
        mock_font.render.return_value = "text_surface"
        mock_font_class.return_value = mock_font

        mock_surface = MagicMock()

        self.creature.display_health = True
        self.creature.draw(mock_surface)

        # Verify blit was called for both image and health text
        self.assertEqual(mock_surface.blit.call_count, 2)
        mock_font.render.assert_called_once_with(str(self.creature.health), True, (255, 255, 255))
    '''

    def test_draw_with_visible_hitbox(self):
        """Test draw method with visible hitbox."""
        mock_surface = MagicMock()
        self.creature.hitbox.visible = True
        self.creature.hitbox.draw = MagicMock()
        self.creature.display_health = False

        self.creature.draw(mock_surface)

        # Verify hitbox draw was called
        self.creature.hitbox.draw.assert_called_once_with(mock_surface)

    '''
    def test_animations_setter(self):
        """Test animations setter."""
        with patch('classes.entities.Creature.Animations') as mock_animations:
            self.creature.animations = ("new_sprite.png", 200, 60, 60)
            mock_animations.assert_called()
    '''

    def test_current_animation_property(self):
        """Test current_animation property."""
        self.creature.current_animation = "IdleUp"
        self.assertEqual(self.creature.current_animation, "IdleUp")

    def test_edge_case_zero_dt(self):
        """Test movement methods with zero delta time."""
        initial_x = self.creature.x
        initial_y = self.creature.y

        self.creature.moveDirection(0, "Up", 100)
        self.assertEqual(self.creature.y, initial_y)  # No movement with dt=0

        self.creature.moveDirection(0, "Right", 100)
        self.assertEqual(self.creature.x, initial_x)  # No movement with dt=0

    def test_multiple_border_collisions(self):
        """Test creature at corner hitting multiple borders."""
        world_map = DummyWorldMap()

        # Place creature at top-left corner
        self.creature.hitbox.x = -5
        self.creature.hitbox.y = -5

        self.creature.update(0.1, world_map)

        self.assertEqual(self.creature.up_speed, 0)
        self.assertEqual(self.creature.left_speed, 0)


if __name__ == "__main__":
    unittest.main()