from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(0, 0)
        self.width = 20

    def move(self):
        self.speed("slow")
        self.forward(5)

    def bounce(self):
        self.setheading(360 - self.heading())
