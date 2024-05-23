from turtle import Turtle

YCOORDS = [-40, -20, 0, 20, 40]


class Paddle:
    def __init__(self, xcor):
        self.paddle_segments = []
        self.create_paddle(xcor)
        self.show_paddle()
        self.paddle_center = self.paddle_segments[2]

    def create_paddle(self, xcor):
        for ycor in YCOORDS:
            new_block = Turtle(shape="square")
            new_block.hideturtle()
            new_block.penup()
            new_block.color("white")
            new_block.speed("fastest")
            new_block.goto(x=xcor, y=ycor)
            self.paddle_segments.append(new_block)

    def show_paddle(self):
        for seg in self.paddle_segments:
            seg.showturtle()
