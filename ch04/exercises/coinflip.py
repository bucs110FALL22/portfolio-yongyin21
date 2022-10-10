
import random
import turtle
window = turtle.Screen()
window.bgcolor('lightblue')
michelangelo = turtle.Turtle()
turtle.speed(0)
distance = 10
angle = 90
is_in_screen = True
colors = ["green","blue","purple"]
while is_in_screen:
  coin = random.randrange(0,2)
  if coin: 
      turtle.right(angle)
  turtle.forward(distance)

  turtleX = turtle.xcor()
  turtleY = turtle.ycor()

  x_range = window.window_height()/2
  y_range = window.window_height()/2

  turtle.color(colors[0])

  colors.append(colors.pop(0))

  if abs(turtleX) > x_range or abs(turtleY) > y_range:
      is_in_screen = False

window.bgcolor("yellow")
window.exitonclick()

