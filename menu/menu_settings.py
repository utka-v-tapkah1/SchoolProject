from src.settings import *


class MenuSettings:
    def __init__(self, infrastructure):
        self.infrastructure = infrastructure
        self.SNAKE_COLOR = settings_db.get_my_skin()
        self.id = settings_db.get_id()
        self.max_id = settings_db.get_max_id()

    def scroll(self):
        pass

    def loop(self):
        return not self.infrastructure.pressed_esc()
