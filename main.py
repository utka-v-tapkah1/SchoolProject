import pygame
from src.game import Game
from src.infrastructure import Infrastructure
from menu.menu import Menu
from menu.menu_settings import MenuSettings
from menu.rules import rules
from src.settings import *

pygame.init()

if __name__ == "__main__":
    screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
    clock = pygame.time.Clock()

    infrastructure = Infrastructure(screen, clock)
    menu_settings = MenuSettings(infrastructure)
    menu = Menu(infrastructure)
    game = Game(infrastructure)

    is_running = True
    is_running_game = False
    is_running_settings = False
    is_running_rules = False
    while is_running:
        screen.fill(SCREEN_COLOR)

        if is_running_game:
            is_running_game = game.loop()
        elif is_running_settings:
            is_running_settings = menu_settings.loop()
        elif is_running_rules:
            is_running_rules = rules(infrastructure)
        else:
            menu.draw_information()

            if menu.start_game():
                game = Game(infrastructure)
                is_running_game = True
            elif menu.is_settings():
                menu_settings = MenuSettings(infrastructure)
                is_running_settings = True
            elif menu.is_rules():
                is_running_rules = True

            is_running = menu.is_exit()  # Проверка на выход через кнопку + отрисовка кнопки

        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

pygame.quit()
