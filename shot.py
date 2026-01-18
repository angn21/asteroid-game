from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
