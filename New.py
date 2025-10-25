import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Endless Colorful Squares")
screen.setup(width=600, height=600)

# List of colors to cycle through
bg_colors = ["lightblue", "lavender", "mintcream", "peachpuff", "honeydew", "mistyrose"]
pen_colors = ["red", "blue", "green", "purple", "orange", "magenta", "cyan", "gold"]

# Create turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(0)  # Fastest speed

# Draw squares forever
while True:
    screen.bgcolor(random.choice(bg_colors))  # Change background color
    t.color(random.choice(pen_colors))        # Change pen color
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)  # Slight rotation to create a spiral effect