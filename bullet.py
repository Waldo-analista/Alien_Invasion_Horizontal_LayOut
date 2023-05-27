import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.settings=settings
        self.screen=screen
        self.ship=ship
        self.color=settings.bullet_color
        self.speed_factor=settings.bullet_factor_velocidad

        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height) #se crea rectangulo
        self.rect.centery=ship.rect.centery
        self.rect.left=ship.rect.right
        self.x=self.rect.x

    def update(self):
        self.x+=self.speed_factor
        self.rect.x=self.x

    def dibujar_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
