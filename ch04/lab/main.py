import pygame
import random
import math
#Part A:
pygame.init()
pygame.display.set_caption("Dartboard")
screen = pygame.display.set_mode((300, 300))
screen.fill((0, 0, 255))
width = screen.get_width() / 2
height = screen.get_height() / 2
pygame.draw.circle(screen, (255,128,128),(width,height), width)
pygame.draw.circle(screen, (255,128,128),(width,height), width)
pygame.draw.line(screen, (255,255,255), (width, 0), (width, height * 2), 2)
pygame.draw.line(screen, (255,255,255), (0, height), (width * 2, height), 2)
pygame.display.flip()  
#Part B
for i in range(10):
  x = random.randrange(0,width)
  y = random.randrange(0, height)
  coordinates = (x,y)
  print(coordinates)
  for i in [coordinates]:
      distance_from_center = math.hypot(x-150, y-150) 
      is_in_circle = distance_from_center <= 300/2 
      if is_in_circle == True:
        pygame.draw.circle(screen, "green", (coordinates), (5))
      if is_in_circle == False:
        pygame.draw.circle(screen, "red", (coordinates), (5))
      pygame.display.flip()
from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()







