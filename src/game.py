import pygame.event
from random import randint
from src.snake import Snake
from src.infrastructure import Infrastructure
from src.settings import *
from src.utils import *


class Game:
    def __init__(self, infrastructure: Infrastructure):
        self.infrastructure = infrastructure
        head = get_center_element()
        self.snake = Snake(head)
        self.apple: Element = gen_apple(self.snake)
        self.coin: Element = False
        self.last_coin: Element = self.coin
        self.tick_counter = 0
        self.tick_counter_coin = 0
        self.score = 0
        self.balance = 0
        self.snake_speed_delay = INITIAL_SPEED_DELAY
        self.is_running = True
        self.is_game_over = False
        self.is_win = False
        self.is_stop = True

    def draw_plus_coin(self):
        self.tick_counter_coin += 1
        self.infrastructure.draw_text("+1", COIN_COLOR, (self.last_coin.x * SCALE + SCALE // 2,
                                                         self.last_coin.y * SCALE - 25))
        if self.tick_counter_coin >= 20:
            self.tick_counter_coin = 0

    def question(self):
        pass
    def process_events(self):
        self.is_running = not self.infrastructure.pressed_esc()
        new_direction = self.infrastructure.key_get_pressed()
        if len(self.snake.snake) <= 1 and new_direction is not None:
            self.is_stop = False
        if new_direction is not None:
            self.snake.set_direction(new_direction)

    def render(self):
        for n, el in enumerate(self.snake.snake):
            if n % 2 == 0:
                self.infrastructure.draw_element(el.x, el.y, ELEMENT_SIZE, RADIUS,
                                                 settings_db.get_my_skin().split(',')[0])
            else:
                self.infrastructure.draw_element(el.x, el.y, ELEMENT_SIZE, RADIUS,
                                                 settings_db.get_my_skin().split(',')[1])

        self.infrastructure.draw_line(0, 0.75, WIDTH, 0.75, BASE_COLOR)
        self.infrastructure.draw_element(self.apple.x, self.apple.y, ELEMENT_SIZE, RADIUS+7, APPLE_COLOR)
        if self.coin:
            self.infrastructure.draw_element(self.coin.x, self.coin.y, ELEMENT_SIZE, 100, COIN_COLOR)
        self.infrastructure.draw_text(f"Счёт: {self.score}", BASE_COLOR, (WIDTH // 2 * SCALE, SCALE * 0.4))
        if self.tick_counter_coin >= 1:
            self.draw_plus_coin()

        if self.is_game_over:
            self.infrastructure.draw_text(f"Конец игры", GAME_OVER_COLOR, (WIDTH // 2 * SCALE, HEIGHT // 2 * SCALE))

    def update_state(self):
        if self.is_stop:
            return
        elif self.is_win:
            if self.score > user_db.get_mscore():
                user_db.upd_mscore(self.score)
            user_db.upd_bal(self.balance)
            user_db.upd_bal(5)
        elif self.is_game_over:
            if self.score > user_db.get_mscore():
                user_db.upd_mscore(self.score)
            user_db.upd_bal(self.balance)
            return

        self.tick_counter += 2
        if not self.tick_counter % self.snake_speed_delay:
            head = self.snake.get_new_head()
            if is_good_head(head, self.snake):
                self.snake.enqueue(head)
                if len(self.snake.snake) >= WIDTH * HEIGHT:  # Победа
                    self.is_game_over = True
                elif head == self.apple:
                    self.score += 1
                    self.apple = gen_apple(self.snake)
                    if randint(1, 7) == 7 and len(self.snake.snake) < WIDTH * HEIGHT - 1:
                        self.coin = gen_coin(self.snake, self.apple)
                    else:
                        self.coin = False
                else:
                    self.snake.dequeue()
                if self.coin:
                    if head == self.coin:
                        self.last_coin = self.coin
                        self.coin = False
                        self.balance += 1
                        self.tick_counter_coin = 1
            else:
                self.is_game_over = True

    def loop(self):
        self.process_events()
        self.update_state()
        self.render()
        return self.is_running
