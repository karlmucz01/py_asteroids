from circleshape import CircleShape
import constants
import pygame


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
    
    def draw(self, screen):
        color = 'white'
        width = 2
        pygame.draw.circle(screen, color=color, center=self.position, radius=self.radius, width=width)
    
    def update(self, dt):
        self.position += self.velocity * dt