from src.settings import *
from src.button import Button


class MenuSettings:
    def __init__(self, infrastructure):
        self.infrastructure = infrastructure
        self.id = settings_db.get_my_id()
        self.max_id = settings_db.get_max_id()
        self.b_next = Button(self.infrastructure, 375, SCALE * 2 + 25,
                             self.infrastructure.font, "Следующий", BASE_COLOR)
        self.b_back = Button(self.infrastructure, 125, SCALE * 2 + 25,
                             self.infrastructure.font, "Предыдущий", BASE_COLOR)
        self.b_take = Button(self.infrastructure, 600, SCALE * 2 + 25,
                             self.infrastructure.font, "Взять", BASE_COLOR)
        self.b_buy = Button(self.infrastructure, 600, SCALE * 2 + 25,
                            self.infrastructure.font, "Купить", BASE_COLOR)

    def scroll_skins(self):
        self.infrastructure.draw_text("Скин", BASE_COLOR, (WIDTH // 2 * SCALE, SCALE))
        if self.b_next.draw():
            if self.id >= self.max_id:
                self.id = 1
            else:
                self.id += 1
        if self.b_back.draw():
            if self.id <= 1:
                self.id = self.max_id
            else:
                self.id -= 1
        self.infrastructure.draw_element(5.90, 1.95, ELEMENT_SIZE, RADIUS, settings_db.get_skin(self.id).split(',')[0])
        if settings_db.skin_in_stock(self.id):
            if self.b_take.draw():
                settings_db.take_skin(self.id)
        else:
            self.infrastructure.draw_text("Цена: 10", BASE_COLOR, (600, SCALE * 2 + 55))
            if self.b_buy.draw() and user_db.get_bal() - 10 >= 0:
                settings_db.buy_skin(self.id)
                user_db.upd_bal(-10)

    def loop(self):
        self.infrastructure.draw_text(f"Баланс: {user_db.get_bal()}", BASE_COLOR, (WIDTH * SCALE - 100, SCALE))
        self.scroll_skins()
        return not self.infrastructure.pressed_esc()
