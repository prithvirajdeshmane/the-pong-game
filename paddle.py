from turtle import Turtle

# directional angles for movement
MOVE_DISTANCE = 20
BOUNDARY_LIMIT = 240


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(xcor, 0)

    def up(self):
        if self.ycor() < BOUNDARY_LIMIT:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > (-1 * BOUNDARY_LIMIT):
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
