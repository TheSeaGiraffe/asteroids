import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    num_pass, num_fail = pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen_coords = screen.fill((0, 0, 0))
        pygame.display.flip()
        time_since_last_tick = clock.tick(60)
        dt = time_since_last_tick / 1000


if __name__ == "__main__":
    main()
