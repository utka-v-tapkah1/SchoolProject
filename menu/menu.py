from src.infrastructure import Infrastructure
from src.settings import *
from src.button import Button


class Menu:
    def __init__(self, infrastructure: Infrastructure):
        self.infrastructure = infrastructure

        self.b_start = Button(self.infrastructure.screen,
                              x=WIDTH // 2 * SCALE, y=SCALE * 4,
                              font=self.infrastructure.font, text="Начать")
        self.b_settings = Button(self.infrastructure.screen,
                              x=WIDTH // 2 * SCALE, y=SCALE * 5,
                              font=self.infrastructure.font, text="Настройки")
        self.b_rules = Button(self.infrastructure.screen,
                              x=WIDTH // 2 * SCALE, y=SCALE * 6,
                              font=self.infrastructure.font, text="Правила")
        self.b_exit = Button(self.infrastructure.screen,
                              x=WIDTH // 2 * SCALE, y=SCALE * 7,
                              font=self.infrastructure.font, text="Выход")

    def start_game(self):
        return self.b_start.draw()

    def is_settings(self):
        return self.b_settings.draw()

    def is_rules(self):
        return self.b_rules.draw()

    def is_exit(self):
        return not self.b_exit.draw()

    def draw_information(self):
        self.infrastructure.draw_text(f"Максимальный счёт: {user_db.get_mscore()}", BASE_COLOR, (WIDTH // 2 * SCALE, 20))
        self.infrastructure.draw_text(f"Баланс: {user_db.get_bal()}", BASE_COLOR, (WIDTH // 2 * SCALE, 20 + SCALE))
