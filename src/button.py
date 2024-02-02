from src.settings import *
import pygame

pygame.init()


class Button:
    def __init__(self, screen, clock, x: int, y: int, font: pygame.font.Font, text: str, color=BASE_COLOR):
        self.screen = screen
        self.clock = clock
        self.color = color
        self.text = font.render(text, True, self.color)
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)
        self.click = False

    def draw(self):
        self.screen.blit(self.text, (self.rect.x, self.rect.y))
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(self.screen, self.color, self.rect, 1)
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.click = True
                action = True
        if not pygame.mouse.get_pressed()[0] and self.click:
            self.click = False
        return action
