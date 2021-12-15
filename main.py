import turtle as t
import random

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        blaze_the_turtle.speed(i)
        blaze_the_turtle.pensize(2)
        blaze_the_turtle.color(random_color())
        blaze_the_turtle.circle(100)
        blaze_the_turtle.setheading(blaze_the_turtle.heading() + size_of_gap)


draw_spirograph(7)

my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
