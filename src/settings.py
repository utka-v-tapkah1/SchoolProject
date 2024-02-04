from db.database import *

WIDTH = 20
HEIGHT = 10
SCALE = 40
RADIUS = 5
ELEMENT_SIZE = 38
FPS = 60

INITIAL_SPEED_DELAY = FPS

APPLE_COLOR = "red"
COIN_COLOR = "gold"
BASE_COLOR = "#efefef"
SCREEN_COLOR = "black"
GAME_OVER_COLOR = "#ff390d"
SKINS = [
    "yellow,#ffe100",
    "green,#04d100",
    "red,#a50000",
    "blue,#0000c1",
    "#ff61f1,#d945cc"
]

user_db = UserDataBase()
questions_db = QuestionsDataBase()
settings_db = SettingsDataBase()
