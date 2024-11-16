import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(- angle) * 1.2
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, velocity1)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)