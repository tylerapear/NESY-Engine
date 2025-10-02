# tests/classes/entities/LogicalSurface.py
import os
import sys
import unittest

# -> HEADLESS / CI: set dummy driver before importing pygame
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame
pygame.init()


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.insert(0, ROOT)  

# Import the class under test
from classes.entities.LogicalSurface import LogicalSurface


class TestLogicalSurface(unittest.TestCase):
    def test_init_and_properties(self):
        ls = LogicalSurface(100, 50, (10, 20, 30))
        self.assertEqual(ls.width, 100)
        self.assertEqual(ls.height, 50)
        self.assertEqual(ls.background_color, (10, 20, 30))
        self.assertIsInstance(ls.surface, pygame.Surface)
        self.assertEqual(ls.surface.get_size(), (100, 50))

    def test_compute_fit_same_size(self):
        ls = LogicalSurface(100, 50, (0, 0, 0))
        scale, x_off, y_off, render_w, render_h = ls.compute_fit(100, 50)
        self.assertAlmostEqual(scale, 1.0)
        self.assertEqual((render_w, render_h), (100, 50))
        self.assertEqual((x_off, y_off), (0, 0))

    def test_compute_fit_smaller(self):
        ls = LogicalSurface(100, 50, (0, 0, 0))
        scale, x_off, y_off, render_w, render_h = ls.compute_fit(50, 25)
        self.assertAlmostEqual(scale, 0.5)
        self.assertEqual((render_w, render_h), (50, 25))
        self.assertEqual((x_off, y_off), (0, 0))

    def test_compute_fit_aspect_diff(self):
        ls = LogicalSurface(100, 50, (0, 0, 0))
        scale, x_off, y_off, render_w, render_h = ls.compute_fit(150, 150)
        # scale = min(150/100=1.5, 150/50=3) => 1.5
        self.assertAlmostEqual(scale, 1.5)
        self.assertEqual((render_w, render_h), (150, 75))
        self.assertEqual((x_off, y_off), (0, (150 - 75) // 2))

    def test_blit_scaled_and_background(self):
        # background should be applied to whole dst; content should be blitted centered
        ls = LogicalSurface(100, 50, (255, 0, 0))  
        ls.surface.fill((0, 255, 0))  

        dst_w, dst_h = 150, 150
        dst = pygame.Surface((dst_w, dst_h))
        dst.fill((0, 0, 0))  

        ls.blit(dst)

        # corners outside rendered area should be background color (red)
        self.assertEqual(dst.get_at((0, 0))[:3], (255, 0, 0))

        # compute where rendered content was placed and check a pixel inside it is green
        _, x_off, y_off, render_w, render_h = ls.compute_fit(dst_w, dst_h)
        inside_x = x_off + max(1, render_w // 4)
        inside_y = y_off + max(1, render_h // 4)
        self.assertEqual(dst.get_at((inside_x, inside_y))[:3], (0, 255, 0))

    def test_blit_unscaled_branch(self):
        # choose a destination such that scale == 1 -> render_w == width & render_h == height
        ls = LogicalSurface(100, 50, (10, 20, 30))
        ls.surface.fill((5, 6, 7))  

        dst = pygame.Surface((100, 150))
        dst.fill((1, 2, 3))

        ls.blit(dst)

        _, x_off, y_off, _, _ = ls.compute_fit(100, 150)
     
        self.assertEqual(dst.get_at((x_off + 2, y_off + 2))[:3], (5, 6, 7))
    
        self.assertEqual(dst.get_at((0, 0))[:3], (10, 20, 30))


if __name__ == "__main__":  
    unittest.main()  
