import pygame
from Creature import Creature
import os

class Player(Creature):

  def moveUp(self, dt, speed):
    self.y -= speed * dt
    if not self.direction == "up":
       self.animationPhase = 0
       self.direction = "up"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Up'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.animationPhase >= len(self.sprites['Up']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1

  def moveDown(self, dt, speed):
    self.y += speed * dt
    if not self.direction == "down":
       self.animationPhase = 0
       self.direction = "down"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Down'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.animationPhase >= len(self.sprites['Down']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1

  def moveLeft(self, dt, speed):
    self.x -= speed * dt
    if not self.direction == "left":
       self.animationPhase = 0
       self.direction = "left"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Left'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.animationPhase >= len(self.sprites['Left']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1

  def moveRight(self, dt, speed):
    self.x += speed * dt
    if not self.direction == "right":
       self.animationPhase = 0
       self.direction = "right"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Right'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.animationPhase >= len(self.sprites['Right']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1