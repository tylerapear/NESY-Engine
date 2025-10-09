# tests/test_tile_unittest.py
"""
Unit tests for the Tile class including edge cases.
These tests mock pygame and the Hitbox class so they run without external assets.
"""
import unittest
from unittest.mock import MagicMock, patch
from classes.entities.Tile import Tile


def get_hitbox_mock(x=0.0, y=0.0, width=10.0, height=10.0):
    """Helper to create a Hitbox mock with specified dimensions."""
    mock_hitbox = MagicMock()
    mock_hitbox.x = x
    mock_hitbox.y = y
    mock_hitbox.width = width
    mock_hitbox.height = height
    mock_hitbox.offset = {"x": x, "y": y, "width": width, "height": height}
    return mock_hitbox

def get_screen_mock(tile_width=16, tile_height=16):
    """Helper to create a screen mock with specified tile dimensions."""
    mock_screen = MagicMock()
    mock_screen.tile_width = tile_width
    mock_screen.tile_height = tile_height
    return mock_screen

class TestTile(unittest.TestCase):
    """Extended unit tests for Tile with edge cases."""

    def setUp(self):
        """Set up test fixtures"""
        self.bg_path = "assets/Tiles/mountain.png"
        self.fg_path = "assets/Tiles/sand.png"
        self.title = Tile(
            background_img_path="assets/Tiles/mountain.png",
            foreground_img_path="assets/Tiles/sand.png",
            hitbox_active=True,
            hitbox_dimentions={"x": 0, "y": 0, "width": 50, "height": 50},
            hitbox_offset={"x": 5, "y": 5, "width": 0, "height": 0},
            hitbox_visible=False
        )

    def test_init(self):
        """Test Tile initialization"""
        self.assertEqual(self.title.background_img_path, "assets/Tiles/mountain.png")
        self.assertIsNotNone(self.title.background_image)
        self.assertEqual(self.title.foreground_img_path, "assets/Tiles/sand.png")
        self.assertIsNotNone(self.title.foreground_image)
        self.assertTrue(self.title.hitbox_active)
        self.assertIsNotNone(self.title.hitbox)
        self.assertEqual(self.title.hitbox.offset, {"x": 5, "y": 5, "width": 0, "height": 0})

    def test_property_setters_getters(self):
        """Test Tile property setters and getters"""
        self.title.background_img_path = "assets/Tiles/sand.png"
        self.assertEqual(self.title.background_img_path, "assets/Tiles/sand.png")

        self.title.foreground_img_path = "assets/Tiles/mountain.png"
        self.assertEqual(self.title.foreground_img_path, "assets/Tiles/mountain.png")

        self.title.hitbox_active = False
        self.assertFalse(self.title.hitbox_active)

        new_hitbox = MagicMock()
        self.title.hitbox = new_hitbox
        self.assertEqual(self.title.hitbox, new_hitbox)

    def test_init_no_foreground(self):
        """Test Tile initialization with no foreground image"""
        tile = Tile(
            background_img_path="assets/Tiles/mountain.png",
            foreground_img_path="",
            hitbox_active=True,
            hitbox_dimentions={"x": 0, "y": 0, "width": 10, "height": 10},
            hitbox_offset={"x": 1, "y": 1, "width": 1, "height": 1},
            hitbox_visible=False
        )
        self.assertEqual(tile.background_img_path, "assets/Tiles/mountain.png")
        self.assertIsNotNone(tile.background_image)
        self.assertEqual(tile.foreground_img_path, "")
        self.assertIsNone(tile.foreground_image)
        self.assertTrue(tile.hitbox_active)
        self.assertIsNotNone(tile.hitbox)
        self.assertEqual(tile.hitbox.offset, {"x": 1, "y": 1, "width": 1, "height": 1})

    def test_init_with_foreground(self):
        """Test Tile initialization with foreground image"""
        tile = Tile(
            background_img_path="assets/Tiles/mountain.png",
            foreground_img_path="assets/Tiles/sand.png",
            hitbox_active=True,
            hitbox_dimentions={"x": 0, "y": 0, "width": 10, "height": 10},
            hitbox_offset={"x": 1, "y": 1, "width": 1, "height": 1},
            hitbox_visible=False
        )
        self.assertEqual(tile.background_img_path, "assets/Tiles/mountain.png")
        self.assertIsNotNone(tile.background_image)
        self.assertEqual(tile.foreground_img_path, "assets/Tiles/sand.png")
        self.assertIsNotNone(tile.foreground_image)
        self.assertTrue(tile.hitbox_active)
        self.assertIsNotNone(tile.hitbox)
        self.assertEqual(tile.hitbox.offset, {"x": 1, "y": 1, "width": 1, "height": 1})

    @patch("classes.entities.Tile.pygame.transform.scale")
    @patch("classes.entities.Tile.pygame.image.load")
    @patch("classes.entities.Tile.Hitbox")
    def test_background_image_load(self, mock_hitbox_cls, mock_image_load, mock_scale):
        """Tile should load background image on init."""
        mock_image_load.return_value = MagicMock()
        mock_hitbox = MagicMock()
        mock_hitbox.offset = {"x": 0, "y": 0, "width": 0, "height": 0}
        mock_hitbox_cls.return_value = mock_hitbox

        tile = Tile(self.bg_path)
        mock_image_load.assert_called_once_with(self.bg_path)
        self.assertIsNotNone(tile.background_image)

    @patch("classes.entities.Tile.pygame.transform.scale")
    @patch("classes.entities.Tile.pygame.image.load")
    @patch("classes.entities.Tile.Hitbox")
    def test_background_scales_and_blits(self, mock_hitbox_cls, mock_image_load, mock_scale):
        """draw_background should scale background to tile size and blit to surface."""
        mock_image_load.return_value = MagicMock()
        mock_hitbox = get_hitbox_mock(0, 0, 0, 0)
        mock_hitbox_cls.return_value = mock_hitbox
        tile = Tile(self.bg_path)
        screen = get_screen_mock()
        surface = MagicMock()

        tile.draw_background(screen, surface, x=5, y=7)

        mock_scale.assert_called_once()
        surface.blit.assert_called_once_with(mock_scale.return_value, (5, 7))

    @patch("classes.entities.Tile.Hitbox")
    @patch("classes.entities.Tile.pygame.transform.scale")
    @patch("classes.entities.Tile.pygame.image.load")
    def test_draw_foreground_hitbox_calculation(self, mock_image_load, mock_scale, mock_hitbox_cls):
        """draw_foreground should set hitbox fields correctly and call hitbox.draw."""
        mock_image_load.return_value = MagicMock()
        mock_scale.return_value = MagicMock()
        mock_hitbox = get_hitbox_mock(0.5, 0.25, 0.5, 0.5)
        mock_hitbox_cls.return_value = mock_hitbox
        tile = Tile(self.bg_path, self.fg_path, hitbox_active=True, hitbox_dimentions={"x":0,"y":0,"width":10,"height":10}, hitbox_offset=mock_hitbox.offset)
        screen = get_screen_mock(40, 20)
        surface = MagicMock()
        x, y = 100, 200

        tile.draw_foreground(screen, surface, x, y)

        expected_x = x + screen.tile_width * mock_hitbox.offset["x"]
        expected_y = y + (screen.tile_height * mock_hitbox.offset["y"])
        expected_w = screen.tile_width * mock_hitbox.offset["width"]
        expected_h = screen.tile_height * mock_hitbox.offset["height"]
        self.assertAlmostEqual(mock_hitbox.x, expected_x)
        self.assertAlmostEqual(mock_hitbox.y, expected_y)
        self.assertAlmostEqual(mock_hitbox.width, expected_w)
        self.assertAlmostEqual(mock_hitbox.height, expected_h)
        mock_hitbox.draw.assert_called_once_with(surface)

    @patch("classes.entities.Tile.Hitbox")
    @patch("classes.entities.Tile.pygame.image.load")
    def test_image_load_failure_raises(self, mock_image_load, mock_hitbox_cls):
        """If pygame.image.load raises an error, Tile initialization should propagate it."""
        import pygame
        mock_image_load.side_effect = pygame.error("cannot load image")

        mock_hitbox = MagicMock()
        mock_hitbox.offset = {"x": 0, "y": 0, "width": 0, "height": 0}
        mock_hitbox_cls.return_value = mock_hitbox

        with self.assertRaises(pygame.error):
            Tile(self.bg_path)

    @patch("classes.entities.Tile.Hitbox")
    @patch("classes.entities.Tile.pygame.transform.scale")
    @patch("classes.entities.Tile.pygame.image.load")
    def test_draw_foreground_negative_offset_edge_case(self, mock_image_load, mock_scale, mock_hitbox_cls):
        """Edge case: negative offsets (should still compute values, possibly negative positions)."""
        mock_image_load.return_value = MagicMock()
        mock_scale.return_value = MagicMock()
        mock_hitbox = get_hitbox_mock(-1, -0.5, 2, 2)
        mock_hitbox_cls.return_value = mock_hitbox
        tile = Tile(self.bg_path, self.fg_path, hitbox_offset=mock_hitbox.offset)
        screen = MagicMock()
        screen.tile_width = 10
        screen.tile_height = 10
        surface = MagicMock()

        tile.draw_foreground(screen, surface, x=0, y=0)

        self.assertEqual(mock_hitbox.x, 0 + screen.tile_width * (-1))
        self.assertEqual(mock_hitbox.y, 0 + screen.tile_height * (-0.5))
        self.assertEqual(mock_hitbox.width, screen.tile_width * 2)
        self.assertEqual(mock_hitbox.height, screen.tile_height * 2)
        mock_hitbox.draw.assert_called_once_with(surface)

    @patch("classes.entities.Tile.Hitbox")
    @patch("classes.entities.Tile.pygame.image.load")
    @patch("classes.entities.Tile.pygame.transform.scale")
    def test_large_tile_size_edge_case(self, mock_image_load, mock_scale, mock_hitbox_cls):
        """Edge case: very large tile sizes — arithmetic should still work and not overflow in normal cases."""
        mock_image_load.return_value = MagicMock()
        mock_scale.return_value = MagicMock()
        mock_hitbox = get_hitbox_mock(0.1, 0.2, 1000, 1000)
        mock_hitbox_cls.return_value = mock_hitbox
        tile = Tile(self.bg_path, self.fg_path, hitbox_offset=mock_hitbox.offset)
        screen =get_screen_mock(10000, 100000)
        surface = MagicMock()

        tile.draw_foreground(screen, surface, x=12345, y=67890)

        self.assertEqual(mock_hitbox.width, screen.tile_width * mock_hitbox.offset["width"])
        self.assertEqual(mock_hitbox.height, screen.tile_height * mock_hitbox.offset["height"])
        mock_hitbox.draw.assert_called_once_with(surface)

    @patch("classes.entities.Tile.Hitbox")
    @patch("classes.entities.Tile.pygame.image.load")
    @patch("classes.entities.Tile.pygame.transform.scale")
    def test_zero_sized_hitbox_edge_case(self, mock_image_load, mock_scale, mock_hitbox_cls):
        """Edge case: zero-sized hitbox — should set width and height to zero."""
        mock_image_load.return_value = MagicMock()
        mock_scale.return_value = MagicMock()
        mock_hitbox = get_hitbox_mock(0, 0, 0, 0)
        mock_hitbox_cls.return_value = mock_hitbox
        tile = Tile(self.bg_path, self.fg_path, hitbox_offset=mock_hitbox.offset)
        screen = get_screen_mock(50, 50)
        surface = MagicMock()

        tile.draw_foreground(screen, surface, x=10, y=10)

        self.assertEqual(mock_hitbox.width, 0)
        self.assertEqual(mock_hitbox.height, 0)
        mock_hitbox.draw.assert_called_once_with(surface)

if __name__ == "__main__":
    unittest.main()
