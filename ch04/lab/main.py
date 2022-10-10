import pygame
import random
import math
#Part A:
pygame.init()
pygame.display.set_caption("Dartboard")
screen = pygame.display.set_mode((300, 300))
screen.fill(("red"))
width = screen.get_width() / 2
height = screen.get_height() / 2
pygame.draw.circle(screen, ("green"),(width,height), width)
pygame.draw.circle(screen, ("green"),(width,height), width)
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
pygame.time.wait(4750)
window = pygame.display.set_mode([300, 300])
window.fill("black")
blue_team = pygame.draw.rect(window, "blue", pygame.Rect(0, 0, 150, 300))
red_team = pygame.draw.rect(window, "red", pygame.Rect(150, 0, 150, 300))
# pygame.draw.rect(window, "red", pygame.Rect(0, 0, 150, 300))
# pygame.draw.rect(window, "blue", pygame.Rect(150, 0, 150, 300))
pygame.display.flip()

blue_points = 0
red_points = 0
player_selected = ""

team_chosen = False
while not team_chosen:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xmouse, ymouse) = pygame.mouse.get_pos()
            if red_team.collidepoint(xmouse, ymouse):
                print("You think Red will win?")
                player_selected = "red"
                team_chosen = True
                pygame.display.flip()
            else:
                print("You think Blue will win?")
                player_selected = "blue"
                team_chosen = True
                pygame.display.flip()
              
window = pygame.display.set_mode([300, 300])
window.fill("blue")
pygame.draw.circle(window, "purple", (150, 150), (150))
pygame.draw.line(window, "black", (0, 150), (300, 150))
pygame.draw.line(window, "black", (150, 0), (150, 300))
pygame.display.flip()


for i in range(10):
    x = random.randrange(0, 301)
    y = random.randrange(0, 301)
    coordinates = [x, y]

    pygame.draw.circle(window, "red", (coordinates), (5))
    for i in [coordinates]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          red_points +=1
        if is_in_circle == False:
            pygame.draw.circle(window, "green", (coordinates), (5))

    x = random.randrange(0, 301)
    y = random.randrange(0, 301)
    coordinates = [x, y]

    pygame.draw.circle(window, "blue", (coordinates), (5))
    for i in coordinates:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          blue_points +=1
        if is_in_circle == False:
            pygame.draw.circle(window, "green", (coordinates), (5))

    pygame.display.flip()

print("Blue had", blue_points)
print("Red had", red_points)

#PartC
if player_selected == "red" and red_points > blue_points:
  print("Player ROJO Wins!")
  print("You Win!")
if player_selected == "red" and red_points < blue_points:
  print("Player AZUL Wins!")
  print("You Lose!")
if player_selected == "blue" and blue_points > red_points:
  print("Player AZUL Wins!")
  print("You Win!")
if player_selected == "blue" and blue_points < red_points:
  print("Player ROJO Wins!")
  print("You Lose!")
if player_selected == "blue" and blue_points == red_points:
  print("Tie Game!")
  print("NO CONTEST")
if player_selected == "red" and red_points == blue_points:
  print("Tie Game!")
  print("NO CONTEST")


from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()







