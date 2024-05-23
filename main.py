from turtle import Screen


""" Screen variables """
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"

# create Game Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pong")




screen.exitonclick()