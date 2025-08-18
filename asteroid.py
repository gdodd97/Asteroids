import pygame
from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    
    def split(self):
        random_angle = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = a * 1.2
            asteroid_b.velocity = b * 1.2
        self.kill()
            

