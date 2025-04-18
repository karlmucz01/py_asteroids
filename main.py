from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot
from sys import exit
import constants
import pygame


def main(): 
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print('Game over!')
                exit()
            for s in shots:
                if asteroid.is_colliding(s):
                    asteroid.split()
                    s.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        updateable.update(dt)
        for curr_drawable in drawable:
            curr_drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()