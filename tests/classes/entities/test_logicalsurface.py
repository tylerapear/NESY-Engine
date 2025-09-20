import pygame
from classes.entities.LogicalSurface import LogicalSurface

def test_compute_fit():
    ls = LogicalSurface(1280, 720, (0, 0, 0))

    # Test same size
    scale, x_off, y_off, rw, rh = ls.compute_fit(1280, 720)
    assert scale == 1
    assert x_off == 0
    assert y_off == 0
    assert rw == 1280
    assert rh == 720

    # Test larger destination
    scale, x_off, y_off, rw, rh = ls.compute_fit(1920, 1080)
    assert scale == 1.5
    assert x_off == 0
    assert y_off == 0
    assert rw == 1920
    assert rh == 1080

def test_blit():
    ls = LogicalSurface(1280, 720, (0, 0, 0))
    surface = pygame.Surface((1920, 1080))

    # Ensure blit runs without errors
    ls.blit(surface)