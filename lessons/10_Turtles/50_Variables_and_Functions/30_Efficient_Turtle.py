
"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):
                          # Move tina forward by the forward distance
   angle =360/sides

   for i in range(sides):
      tina.forward(100)
      tina.left(angle)                                 # Turn tina left by the left turn


                                     # Move tina to another spot on the screen

draw_polygon(4)                        # Draw a pentagon

tina.penup()
tina.goto(200, 200)
tina.pendown
                                    # Move tina to another spot on the screen

draw_polygon(5) 
tina.penup()
tina.goto(200, 0)
tina.pendown                      # Draw a hexagon

turtle.exitonclick()                     # Close the window when we click on it