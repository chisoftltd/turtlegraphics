import turtle as t
import random

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


blaze_the_turtle.resizemode("auto")
directions = [0, 45, 90, 135, 180, 225, 270]

for i in range(70):
    blaze_the_turtle.speed(i)
    blaze_the_turtle.pensize(i)
    blaze_the_turtle.color(random_color())
    blaze_the_turtle.forward(30)
    blaze_the_turtle.setheading(random.choice(directions))

my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
