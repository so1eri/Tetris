import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((200, 400))
pygame.display.set_caption('Hello World!')

def draw_lines():
    global screen
    for i in range(0, 11):
        pygame.draw.line(screen, (255, 255, 255), (i*20, 0), (i*20, 400))
    for i in range (0, 41):
        pygame.draw.line(screen, (255, 255, 255), (0, i*20), (400, i*20))
    pygame.draw.line(screen, (255, 255, 255), (199, 0), (199, 400))
    pygame.draw.line(screen, (255, 255, 255), (0, 399), (200, 399))
        
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

           
   #10 x 40
   #Draw
   draw_lines()
   pygame.display.update()
    
