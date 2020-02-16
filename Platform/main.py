import pygame
import time
from update_btn import main
from search_btn import search



def mainfile():
      pygame.init()
      screen_size_x = 800
      screen_size_y = 600
      pygame.display.set_caption('NTU Campus Bus Vacancy Checker')
      screen = pygame.display.set_mode((screen_size_x,screen_size_y))

      def button_img(img, img_hover, pos_x, pos_y, task = None):
            img_pos = img.get_rect()
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (pos_x<mouse_pos[0]<(pos_x+img_pos[2])) and (pos_y<mouse_pos[1]<(pos_y+img_pos[3])):
                  screen.blit(img_hover, (pos_x, pos_y))
                  if click[0]==1 and task!= None:
      
                      if task == "search":
                          pygame.quit()
                          search()
                          quit()
                            
            else:
                  screen.blit(img, (pos_x,pos_y))

      def introduction():
            introScreenImage = pygame.image.load("images/hack.png")
            introScreenImage = pygame.transform.scale(introScreenImage, (1000,650))
            start_but=pygame.image.load("images/Picture1.png")
            start_but_big = pygame.image.load("images/Picture2.png")
            screen.blit(introScreenImage,(0,0))
            while True:
                  for event in pygame.event.get():      
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                  button_img(start_but_big,start_but, screen_size_x//5, 2.9*screen_size_y//4, task = "search")
                  pygame.display.flip()

            
      introduction()
mainfile()
