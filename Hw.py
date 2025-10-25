import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Square with Turtle")
screen.setup(width=600, height=600)

# List of colors to cycle through
bg_colors = ["lightblue", "lavender", "mintcream", "peachpuff", "honeydew", "mistyrose"]
pen_colors = ["red", "blue", "green", "purple", "orange", "magenta", "cyan", "gold"]

# Create turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(3)

# Draw square with changing colors
for i in range(4):
    screen.bgcolor(random.choice(bg_colors))  # Change background color
    t.color(random.choice(pen_colors))        # Change pen color
    t.forward(200)
    t.right(90)

# Hide turtle and finish
t.hideturtle()
screen.mainloop()