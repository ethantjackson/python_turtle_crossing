from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"level: {self.level}", font=FONT)

    def increment_level(self):
        self.level += 1
        self.print_level()

    def print_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
