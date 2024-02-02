import pygame
from src.settings import *

pygame.init()


def rules(infrastructure):
    infrastructure.draw_text(
        "1. Управление осуществляется стрелочками", BASE_COLOR, (WIDTH // 2 * SCALE, 50)
    )
    infrastructure.draw_text(
        "2. Запрещается быстро нажимать на клавиши", BASE_COLOR, (WIDTH // 2 * SCALE, 125)
    )
    infrastructure.draw_text(
        "3. Выход в меню - Esc", BASE_COLOR, (WIDTH // 2 * SCALE, 200)
    )
    infrastructure.draw_text(
        "4. При выходе в меню во время игры,", BASE_COLOR, (WIDTH // 2 * SCALE, 275)
    )
    infrastructure.draw_text(
        "прогресс не сохраняется", BASE_COLOR, (WIDTH // 2 * SCALE, 325)
    )
    return not infrastructure.pressed_esc()
