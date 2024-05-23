from turtle import Turtle

# directional angles for movement
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle:
    paddle = None

    def __init__(self, xcor):
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.hideturtle()
        self.paddle.goto(xcor, 0)
        self.paddle.showturtle()

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVE_DISTANCE)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVE_DISTANCE)
