import pygame
from classes.entities.Creature import Creature
import os

class Player(Creature):

  def moveUp(self, dt, speed):
    self.y -= speed * dt
    if not self.direction == "up":
      self.image = self.animations.getNextImage('Up', True)
      self.direction = "up"
    else:
      self.image = self.animations.getNextImage('Up')

  def moveDown(self, dt, speed):
    self.y += speed * dt
    if not self.direction == "down":
      self.image = self.animations.getNextImage('Down', True)
      self.direction = "down"
    else:
      self.image = self.animations.getNextImage('Down')

  def moveLeft(self, dt, speed):
    self.x -= speed * dt
    if not self.direction == "left":
      self.image = self.animations.getNextImage('Left', True)
      self.direction = "left"
    else:
      self.image = self.animations.getNextImage('Left')

  def moveRight(self, dt, speed):
    self.x += speed * dt
    if not self.direction == "right":
      self.image = self.animations.getNextImage('Right', True)
      self.direction = "right"
    else:
      self.image = self.animations.getNextImage('Right')