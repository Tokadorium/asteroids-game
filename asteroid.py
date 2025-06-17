import pygame
import random

from circleshape import CircleShape

from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20, 50)
        vectorA = self.velocity.rotate(new_angle)
        vectorB = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroidA = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidB = Asteroid(self.position.x, self.position.y, new_radius)

        asteroidA.velocity = vectorA * 1.2
        asteroidB.velocity = vectorB * 1.2