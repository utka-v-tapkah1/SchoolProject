from random import randrange
from src.element import Element
from src.snake import Snake
from src.settings import *


def gen_random_element() -> Element:
    return Element(randrange(0, WIDTH), randrange(1, HEIGHT))


def get_center_element() -> Element:
    return Element(WIDTH // 2, HEIGHT // 2)


def is_field_containts(element: Element) -> bool:
    return 0 <= element.x < WIDTH and 1 <= element.y < HEIGHT


def is_good_head(head: Element, snake: Snake) -> bool:
    return is_field_containts(head) and not snake.is_contains(head)


def gen_apple(snake: Snake) -> Element:
    candidate = None
    while candidate is None:
        candidate = gen_random_element()
        if snake.is_contains(candidate):
            candidate = None
    return candidate


def gen_coin(snake: Snake, apple) -> Element:
    candidate = None
    while candidate is None:
        candidate = gen_random_element()
        if snake.is_contains(candidate) or candidate == apple:
            candidate = None
    return candidate
