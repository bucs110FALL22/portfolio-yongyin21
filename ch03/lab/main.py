import turtle #1. import modules
import random
import pygame
import math
pygame.init()
window = pygame.display.set_mode()
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

#list = (range(1,101 ))
#numero = int(numero)
#michelangelo.forward (random.randrange(1,100))
#leonardo.forward(random.randrange(1,100))
#michelangelo.goto(-100,20)
#leonardo.goto(-100,-20)
for i in range(10):
  michelangelo.forward (random.randrange(0,10))
for i in range(10):
  leonardo.forward (random.randrange(0,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# PART B - complete part B here
pygame.draw.circle(window,(30,300,25)(200,20), 20, 5 )

window.exitonclick()
