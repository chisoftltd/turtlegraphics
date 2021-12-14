
from turtle import Turtle, Screen

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = Turtle()

print(blaze_the_turtle)
blaze_the_turtle.shape("arrow")
blaze_the_turtle.color("blue")
blaze_the_turtle.resizemode("auto")

# for i in range(5):
blaze_the_turtle.forward(90)
blaze_the_turtle.right(45)
blaze_the_turtle.forward(110)
blaze_the_turtle.right(45)
blaze_the_turtle.forward(-75)
blaze_the_turtle.right(90)
blaze_the_turtle.forward(75)
blaze_the_turtle.left(45)
blaze_the_turtle.backward(200)
blaze_the_turtle.left(-90)
blaze_the_turtle.backward(100)











my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()