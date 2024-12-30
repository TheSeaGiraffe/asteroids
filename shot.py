import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt