from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.random_color())
        self.firstcolor = self.random_color()
        self.color(self.firstcolor)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)

    def random_color(self):
        r = (random.randint(0, 255))
        g = (random.randint(0, 255))
        b = (random.randint(0, 255))
        color = (r, g, b)
        return color

    def apply_color_to_food(self, snake_new_color):
        self.firstcolor = snake_new_color
        self.color(snake_new_color)
