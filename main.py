import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidFields
from shot import Shot

from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidFields.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidFields()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if player.isColliding(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.isColliding(asteroid):
                    asteroid.kill()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # tick returns ms since last call. Converting this value to seconds and
        # saving it in dt (delta time)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
