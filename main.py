import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    # Init all pygame objects
    num_pass, num_fail = pygame.init()  # Don't do anything with return values just yet
    print("Starting asteroids!")

    # Init clock
    clock = pygame.time.Clock()
    dt = 0

    # Create pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Init screen and player
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    # asteroid_field = AsteroidField()
    _ = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill((0, 0, 0))
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.has_collided(player):
                print("Game over!")
                sys.exit(1)
        pygame.display.flip()
        time_since_last_tick = clock.tick(60)
        dt = time_since_last_tick / 1000


if __name__ == "__main__":
    main()
