from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake Movement ------------------------
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
# --------------------------------------

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Detect Food Collision
    if snake.head.distance(food) < 15:
        snake.extend(food.firstcolor)
        scoreboard.increase_score()
        snake_new_color = food.random_color()
        food.refresh()
        food.apply_color_to_food(snake_new_color)

    # Detect Collision with wall.
    if (snake.head.xcor() > 285) or (snake.head.xcor() < -285) or (snake.head.ycor() > 285) or \
            (snake.head.ycor() < -285):
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with tail.
    for segment in snake.player_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
