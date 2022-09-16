import turtle
my_turtle = turtle.Turtle()
my_turtle.color("purple")
my_turtle.shape("turtle")
num_sides = int(input("Please enter the number of sides"))
length = int(input("Please enter the side length"))
angle = 360 / num_sides

for i in [angle]*num_sides:

        my_turtle.forward(length)
        my_turtle.left(i) 
turtle.done()