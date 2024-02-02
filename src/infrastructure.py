import pygame
from src.directions import Direction
from src.settings import *


class Infrastructure:
    def __init__(self, screen, clock):
        pygame.init()
        self.font = pygame.font.Font(None, SCALE)
        self.screen: pygame.surface.Surface = screen
        self.clock = clock

    def key_get_pressed(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT
        return None

    def draw_line(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.screen, color,
                         start_pos=(x1 * SCALE, y1 * SCALE),
                         end_pos=(x2 * SCALE, y2 * SCALE))

    def draw_element(self, x, y, size, radius, color, img=False):
        if img:
            pass
        else:
            pygame.draw.rect(
                self.screen,
                color,
                (x * SCALE, y * SCALE, size, size),
                0,
                radius,
            )

    def draw_text(self, text, color, coord) -> None:
        message = self.font.render(text, True, color)
        self.screen.blit(
            message,
            message.get_rect(center=coord),
        )

    def pressed_esc(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            return True
        return False
