import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    green_turtle = turtle.Turtle()
    # This code sets our shape to a turtle
    green_turtle.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    green_turtle.speed(1)
    # Set your turtle's color using .color('green')
    green_turtle.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        green_turtle.color(get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        green_turtle.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        green_turtle.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        green_turtle.turtlesize(stretch_wid=i+1, stretch_len=i+1, outline=4)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
