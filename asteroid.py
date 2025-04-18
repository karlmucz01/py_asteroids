from circleshape import CircleShape
import constants
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color = 'white'
        width = 2
        pygame.draw.circle(screen, color=color, center=self.position, radius=self.radius, width=width)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        rand_ang = random.uniform(20, 50)
        velocity1, velocity2 = self.velocity.rotate(rand_ang), self.velocity.rotate(-rand_ang)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = velocity1 * 1.2
        ast2.velocity = velocity2 * 1.2

    