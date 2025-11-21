import unittest
import pygame

from classes.effects.Animation import Animation, DamangePhase

class TestAnimation(unittest.TestCase):
    
    def setUp(self):
        self.animation = Animation(
            spritePath = "./tests/classes/effects/TestSprites", 
            speed = 10, 
            width = 250, 
            height = 250
        )
    
    def test_load_images(self):
        images = self.animation.load_images(self.animation.spritePath)
        self.assertEqual(["./tests/classes/effects/TestSprites/Test1.png", "./tests/classes/effects/TestSprites/Test2.png"], images)
        
    def test_update(self):
        FRAMERATE = 60
        immunity_count = 0
        
        ### After 49 frames, the animation should still be on phase 0
        for i in range(49):
            self.animation.update(FRAMERATE)
        self.assertEqual(self.animation.frame_count, 49)
        self.assertEqual(self.animation.phase, 0)
        self.assertEqual(self.animation.current_image_path, "./tests/classes/effects/TestSprites/Test1.png")
        
        ### After the 50th frame, the phase should increment to 1 and the frame_count should reset
        self.animation.update(FRAMERATE)
        self.assertEqual(self.animation.frame_count, 0)
        self.assertEqual(self.animation.phase, 1)
        self.assertEqual(self.animation.current_image_path, "./tests/classes/effects/TestSprites/Test2.png")
        
        ### After another 50 frames, the phase should change again, back to 0 since there are only 2 images
        for i in range(50):
            self.animation.update(FRAMERATE)
        self.assertEqual(self.animation.frame_count, 0)
        self.assertEqual(self.animation.phase, 0)
        self.assertEqual(self.animation.current_image_path, "./tests/classes/effects/TestSprites/Test1.png")
        
    def test_get_damage_phase(self):
        immunity_count = 0
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.NONE)
        
        immunity_count = 29
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.FIRST)
        
        immunity_count = 25
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.SECOND)
        
        immunity_count = 18
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.THIRD)
        
        immunity_count = 16
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.FOURTH)
        
        immunity_count = 15
        damange_phase = self.animation.get_damage_phase(immunity_count)
        self.assertEqual(damange_phase, DamangePhase.NONE)
        
        