import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(angle)
        asteroid2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = asteroid1_velocity * 1.2
        asteroid2.velocity = asteroid2_velocity * 1.2

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
