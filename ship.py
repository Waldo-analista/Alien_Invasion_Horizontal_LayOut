import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,settings,screen,path_image):
        super().__init__()
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.settings=settings


        self.image=pygame.image.load(path_image)
        self.rect=self.image.get_rect()


        self.rect.x=0
        self.rect.centery=self.screen_rect.centery
        self.y=self.rect.centery

        self.up_move=False
        self.down_move=False

    def dibujar_ship(self):
        self.screen.blit(self.image,self.rect)  #dibuja la imagen en la screen en la posicion indicada por el rectangulo

    def mov_continuo(self):
        if self.up_move:
            if (self.y-self.rect.height/2)>=0:
                self.y-=self.settings.ship_speed_factor
                self.rect.centery=self.y 
        if self.down_move:
            if (self.y+self.rect.height/2) <=self.screen_rect.height:
                self.y+=self.settings.ship_speed_factor
                self.rect.centery=self.y

    def center_ship(self):
        self.rect.centery=self.screen_rect.centery