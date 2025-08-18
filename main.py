import sys
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():

    #initial variables and groups
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroidField = AsteroidField()



    #print screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


        

if __name__ == "__main__":
    main()
