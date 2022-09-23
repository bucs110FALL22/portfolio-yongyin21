import turtle #1. import modules
import random
import pygame
import math

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
#METHOD 1
list = (range(1,101 ))
michelangelo.forward (random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#METHOD 2
for i in range(10):
  leonardo.forward (random.randrange(0,11))
  michelangelo.forward (random.randrange(0,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

def shape_points(num_sides):
  coords = []
  num_sides = num_sides
  side_length = 50
  offset = 100
  for i in range(num_sides):
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x,y])
  return coords
    
pygame.draw.polygon(window,"red", shape_points(3))
pygame.display.flip()
pygame.time.delay(300)
window.fill("red")

pygame.draw.polygon(window,"blue", shape_points(4))
pygame.display.flip()
pygame.time.delay(300)
window.fill("blue")

pygame.draw.polygon(window,"green", shape_points(6))
pygame.display.flip()
pygame.time.delay(300)
window.fill("green")

pygame.draw.polygon(window,"purple", shape_points(9))
pygame.display.flip()
pygame.time.delay(300)
window.fill("purple")

pygame.draw.polygon(window,"orange", shape_points(360))
pygame.display.flip()
pygame.time.delay(300)
window.fill("orange")

#window.exitonclick()
