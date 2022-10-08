import pygame
import math
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

pygame.display.get_window_size()
print(pygame.display.get_window_size())