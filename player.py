from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.respawn()
        self.setheading(90)

    def respawn(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(20)
