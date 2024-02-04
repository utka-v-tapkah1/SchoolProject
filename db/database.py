import sqlite3
from src.settings import *


class UserDataBase:
    def __init__(self):
        self.connection = sqlite3.connect('snake.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS User (
                            balance INTEGER NOT NULL DEFAULT 0,
                            max_score INTEGER NOT NULL DEFAULT 0
                        )
                        ''')
        if self.cursor.execute('SELECT balance FROM User').fetchone() is None:
            self.cursor.execute('INSERT INTO User (balance, max_score) VALUES (0, 0)')
        self.connection.commit()

    def upd_bal(self, x: int):
        self.cursor.execute(f'UPDATE User SET balance = balance + {x}')
        self.connection.commit()

    def get_bal(self):
        return self.cursor.execute('SELECT balance FROM User').fetchone()[0]

    def upd_mscore(self, x: int):
        self.cursor.execute(f'UPDATE User SET max_score = {x}')
        self.connection.commit()

    def get_mscore(self):
        return self.cursor.execute('SELECT max_score FROM User').fetchone()[0]

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


class QuestionsDataBase:
    def __init__(self):
        self.connection = sqlite3.connect('snake.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Questions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question TEXT NOT NULL,
                            t_answer INTEGER NOT NULL,
                            answer1 TEXT NOT NULL,
                            answer2 TEXT NOT NULL,
                            answer3 TEXT NOT NULL,
                            answer4 TEXT NOT NULL
                        )
                        ''')
        questions = [
            ["Какова доля азота в атмосфере?", 1, "78%", "12%", "31%", "96%"],
            ["Сколько ребер у куба?", 1, "12", "6", "8", "4"],
            ["Какую религию исповедовали в Древнем Китае?", 3, "Христианство", "Ислам", "Буддизм", "Иудаизм"],
            ["Кому принадлежит фраза - Карету мне! Карету!?", 1, "Чацкому", "Болконскому", "Обломову", "Онегину"]
        ]
        if self.cursor.execute('SELECT question FROM Questions').fetchone() is None:
            for question in questions:
                self.cursor.execute('''INSERT INTO Questions (question, t_answer, answer1, answer2, answer3, answer4)
                                    VALUES (?, ?, ?, ?, ?, ?)''', question)
        self.connection.commit()

    def get_question(self, x):
        return self.cursor.execute(f'SELECT question FROM Questions WHERE id == {x}').fetchone()[0]

    def get_answer(self, x):
        return self.cursor.execute(f'SELECT t_answer FROM Questions WHERE id == {x}').fetchone()[0]

    def get_max_id(self):
        return len(self.cursor.execute('SELECT id FROM Questions').fetchall())

    def get_all_answers(self, x):
        return self.cursor.execute(f'SELECT answer1, answer2, answer3, answer4 FROM Questions WHERE id == {x}').fetchone()

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


class SettingsDataBase:
    def __init__(self):
        self.connection = sqlite3.connect('snake.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Settings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            in_stock BOOLEAN NOT NULL,
                            skin TEXT NOT NULL,
                            it BOOLEAN NOT NULL
                        )
                        ''')
        skins = [
            "yellow,#ffe100",
            "green,#04d100",
            "red,#a50000",
            "blue,#0000c1",
            "#ff61f1,#d945cc"
        ]
        if self.cursor.execute('SELECT id FROM Settings').fetchone() is None:
            self.cursor.execute(f'INSERT INTO Settings (in_stock, skin, it) VALUES (1, "{skins[0]}", 1)')
            for skin in skins[1:]:
                self.cursor.execute(f'INSERT INTO Settings (in_stock, skin, it) VALUES (0, "{skin}", 0)')
        self.connection.commit()

    def skin_in_stock(self, x):
        return self.cursor.execute(f'SELECT in_stock FROM Settings WHERE id == {x}').fetchone()[0]

    def get_skin(self, x):
        return self.cursor.execute(f'SELECT skin FROM Settings WHERE id == {x}').fetchone()[0]

    def get_my_skin(self):
        return self.cursor.execute(f'SELECT skin FROM Settings WHERE it == 1').fetchone()[0]

    def take_skin(self, x):
        self.cursor.execute(f'UPDATE Settings SET it = 0 WHERE id == {self.get_my_id()}')
        self.cursor.execute(f'UPDATE Settings SET it = 1 WHERE id == {x}')
        self.connection.commit()

    def buy_skin(self, x):
        self.cursor.execute(f'UPDATE Settings SET it = 0 WHERE it == 1')
        self.cursor.execute(f'UPDATE Settings SET it = 1 WHERE id == {x}')
        self.cursor.execute(f'UPDATE Settings SET in_stock = 1 WHERE id == {x}')
        self.connection.commit()

    def get_my_id(self):
        return self.cursor.execute(f'SELECT id FROM Settings WHERE skin == "{self.get_my_skin()}"').fetchone()[0]

    def get_max_id(self):
        return len(self.cursor.execute('SELECT id FROM Settings').fetchall())

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
