import pygame.font
from pygame.sprite import Group
from ship import Ship

class Tablero:
    def __init__(self,settings,screen,stats):
        self.screen=screen
        self.rect_screen=screen.get_rect()
        self.settings=settings
        self.stats=stats

        self.text_color=0,0,255
        self.font=pygame.font.SysFont(None,48)


    def show_score(self):
        score_str=str('Score: '+'{:,}'.format(self.stats.score))
        self.score_image=self.font.render(score_str,True,(255,137,26),self.settings.background_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.top=self.rect_screen.top+5
        self.score_image_rect.right=self.rect_screen.right-25
        self.screen.blit(self.score_image,self.score_image_rect)

        high_score_str=str('High Score: '+'{:,}'.format(self.stats.high_score))
        self.high_score_image=self.font.render(high_score_str,True,(4,159,21),self.settings.background_color)
        self.high_score_image_rect=self.high_score_image.get_rect()
        self.high_score_image_rect.right=self.rect_screen.centerx-10
        self.high_score_image_rect.bottom=self.rect_screen.bottom
        self.screen.blit(self.high_score_image,self.high_score_image_rect)

        level_str=str('Level: '+'{:,}'.format(self.stats.level))
        self.level_image=self.font.render(level_str,True,(255,0,0),self.settings.background_color)
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.top=self.score_image_rect.bottom
        self.level_image_rect.right=self.rect_screen.right-25
        self.screen.blit(self.level_image,self.level_image_rect)

        h_level_str=str('High Level: '+'{:,}'.format(self.stats.high_level))
        self.h_level_image=self.font.render(h_level_str,True,(255,0,0),self.settings.background_color)
        self.h_level_image_rect=self.h_level_image.get_rect()
        self.h_level_image_rect.bottom=self.rect_screen.bottom
        self.h_level_image_rect.left=self.rect_screen.centerx+10
        self.screen.blit(self.h_level_image,self.h_level_image_rect)        
    
        label_ship_str=str('Naves en reserva: '+'{:,}'.format(self.stats.ships_left))
        self.label_ship_image=self.font.render(label_ship_str,True,(255,0,0),self.settings.background_color)
        self.label_ship_image_rect=self.label_ship_image.get_rect()
        self.label_ship_image_rect.top=self.rect_screen.top+5
        self.label_ship_image_rect.left=self.rect_screen.left
        self.screen.blit(self.label_ship_image,self.label_ship_image_rect)

        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.settings,self.screen,'images/picture.bmp')
            ship.rect.top=self.rect_screen.top+5
            ship.rect.left=self.label_ship_image_rect.right+5+2*ship_number*(ship.rect.width)
            self.ships.add(ship)
        self.ships.draw(self.screen)