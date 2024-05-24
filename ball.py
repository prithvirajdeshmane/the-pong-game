from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(0, 0)
        self.width = 20

    def move(self, heading):
        self.setheading(heading)
        self.speed("slow")
        self.forward(1)
