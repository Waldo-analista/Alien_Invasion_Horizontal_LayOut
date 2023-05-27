import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,settings,screen):
        super().__init__()
        self.screen=screen
        self.settings=settings
        
        self.image=pygame.image.load('images/shipinvasor.bmp')
        self.rect=self.image.get_rect()   


        self.x=self.rect.x
        self.y=self.rect.y

    def dibujar_alien(self):
        self.screen.blit(self.image,self.rect)   

    def update(self):
        self.y+=self.settings.alien_speed_factor*self.settings.fleet_direccion
        self.rect.y=self.y

