from collections import defaultdict
import pygame
def algorithm(n): 
  count = 0
  while n > 1: 
    if n % 2 == 0: 
      n /= 2
    else: 
      n = 3 * n + 1
    print (n)
    count += 1
  return count
def makedictionary(upper_Limit):
  max_val = 0
  upper_limit = upper_Limit
  lower_limit = 2
  iters = {}
  iters = defaultdict(list)
  for i in range (lower_limit,upper_limit):
    if algorithm (i) > max_val: 
      max_val = algorithm (i)
    iters [int(i)].append(int(algorithm(i)))
  return iters , max_val
  pygame.init()
  pygame.display.init()
  upper_limit = 20
  lower_limit = 2
  iters, max_val = makedictionary(upper_limit)
  max_so_far = 0
  scale = 5
  display = pygame.display.set_mode()
  font = pygame.font.Font(None, 13)
  list = list(iters.items())
