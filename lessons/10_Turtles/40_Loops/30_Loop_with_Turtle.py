
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina                          # Turn tina left by the left turn
for i in range(6):                       # Loop 4 times for the 4 sides of the square
    tina.forward(150)                    # Move tina forward by 150 pixels
    tina.left(60)
turtle.exitonclick()