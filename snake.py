from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.player_body = []
        self.create_snake()
        self.head = self.player_body[0]
        self.behind = self.player_body[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(position)
            self.player_body.append(body)

    def extend(self, snake_new_color):
        self.player_body[-1].position()
        body = Turtle("square")
        body.color(snake_new_color)
        body.penup()
        body.goto(x=1000, y=1000)
        self.player_body.append(body)

    def snake_move(self):
        for body_nr in range(len(self.player_body) - 1, 0, -1):
            new_x = self.player_body[body_nr - 1].xcor()
            new_y = self.player_body[body_nr - 1].ycor()
            self.player_body[body_nr].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movements
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
