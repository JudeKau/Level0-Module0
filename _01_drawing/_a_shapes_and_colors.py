import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
jude_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
jude_turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
jude_turtle.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
jude_turtle.color('green')
jude_turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
jude_turtle.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
jude_turtle.left(90)
jude_turtle.right(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range(4):
    jude_turtle.forward(100)
    jude_turtle.right(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
jude_turtle.goto(4, 5)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
jude_turtle.begin_fill()
jude_turtle.circle(9, steps=30)
jude_turtle.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!
jude_turtle.color('red')
jude_turtle.begin_fill()
jude_turtle.circle(9, steps=30)
jude_turtle.end_fill()
jude_turtle.color('blue')
jude_turtle.begin_fill()
jude_turtle.circle(9, steps=30)
jude_turtle.end_fill()
jude_turtle.color('yellow')
jude_turtle.begin_fill()
jude_turtle.circle(9, steps=30)
jude_turtle.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
