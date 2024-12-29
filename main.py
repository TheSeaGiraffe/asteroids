import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    # Init all pygame objects
    num_pass, num_fail = pygame.init()  # Don't do anything with return values just yet
    print("Starting asteroids!")

    # Init screen and player
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    player = Player(x, y)

    # Init clock
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # screen_coords = screen.fill((0, 0, 0))
        _ = screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        time_since_last_tick = clock.tick(60)
        dt = time_since_last_tick / 1000


if __name__ == "__main__":
    main()
