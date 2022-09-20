import pygame
pygame.init()
window = pygame.display.set_mode()
pygame.draw.polygon(window, (255,255,255),[(20, 40), (0, 40), (30, 50)])
black = [0,0,0]
pygame.draw.polygon(window,black,[(152, 190), (152, 230), (1056, 230),(1056, 190)],True)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()