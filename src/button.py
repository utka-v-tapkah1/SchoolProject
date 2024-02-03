from src.settings import *
import pygame

pygame.init()


class Button:
    def __init__(self, infrastructure, x: int, y: int, font: pygame.font.Font, text: str, color=BASE_COLOR):
        self.infrastructure = infrastructure
        self.color = color
        self.text = font.render(text, True, self.color)
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)
        self.click = False

    def draw(self):
        self.infrastructure.screen.blit(self.text, (self.rect.x, self.rect.y))
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(self.infrastructure.screen, self.color, self.rect, 1)
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.click = True
            if not pygame.mouse.get_pressed()[0] and self.click:
                self.click = False
                action = True
        return action
