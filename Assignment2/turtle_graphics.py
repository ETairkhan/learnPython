import turtle
import random

def draw_pattern(repetitions, size_increment):
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    # Define a list of colors
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

    # Draw the pattern
    for i in range(repetitions):
        t.color(random.choice(colors))  # Pick a random color
        t.circle(50 + size_increment * i)  # Draw a circle with increasing size
        t.right(360 / repetitions)  # Rotate the turtle for the next circle

    # Complete the drawing
    t.hideturtle()
    screen.mainloop()

# Ask the user for inputs
repetitions = int(input("Enter the number of repetitions (e.g., 36): "))
size_increment = int(input("Enter the size increment for each repetition (e.g., 10): "))

# Call the function to draw the pattern
draw_pattern(repetitions, size_increment)
