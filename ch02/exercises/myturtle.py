import turtle              
my_turtle = turtle.Turtle()
my_turtle.color("purple")
#my_turtle.forward(50)
my_turtle.shape("turtle")
#my_turtle.left(100)
num_sides = int(input("Please enter the number of sides"))
length = 50 
angle = 360 / num_sides

for i in [angle]*num_sides:

        my_turtle.forward(length)
        my_turtle.left(i)  
#my_turtle.left(90)
my_turtle.color("red")

my_turtle.penup()
my_turtle.forward(100)

my_turtle.pendown()
num_sides = int(input("Please enter the number of sides"))
length = 50 
angle = 360 / num_sides

for i in [angle]*num_sides:

        my_turtle.forward(length)
        my_turtle.left(i)  

#my_turtle.forward(30)
#my_turtle.color("yellow")
turtle.done()
