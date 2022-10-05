
import random
import turtle
window = turtle.Screen()
window.bgcolor('lightblue')
michelangelo = turtle.Turtle()
coin_flip = random.choices(["heads", "tails"], [5,5])[0]

if coin_flip == "tails":
  michelangelo.left(90)
  michelangelo.forward(50)
if coin_flip == "heads":
  michelangelo.right(90)
  michelangelo.forward(50)
