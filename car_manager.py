import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

turtle.colormode(255)


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []

    def make_car(self):
        t = turtle.Turtle()
        t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.shape("square")
        t.shapesize(1, 2)
        t.penup()
        t.setheading(180)
        t.goto(320, random.randint(-250, 250))
        self.cars.append(t)

    def random_car(self):
        if random.randint(1, 10) == 1:
            self.make_car()

    def move_cars(self):
        for car in self.cars:
            car.forward(5)
            if car.xcor() < -320:
                self.cars.remove(car)
                car.ht()

    def reset_cars(self):
        for car in self.cars:
            car.ht()
        self.cars.clear()
