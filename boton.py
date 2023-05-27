import pygame.font

class Boton:
    def __init__(self,settings,screen,mensaje):
          self.screen=screen
          self.rect_screen=screen.get_rect()

          self.settings=settings
          self.mensaje=mensaje

          self.width=300
          self.height=50

          self.button_color=255,0,0
          self.text_color=255,255,255
          self.font=pygame.font.SysFont(None,40)

          self.msg_image=self.font.render(mensaje,True,self.text_color,self.button_color)
          self.msg_image_rect=self.msg_image.get_rect()
          self.msg_image_rect.center=self.rect_screen.center


          self.rect=pygame.Rect(0,0,self.width,self.height)
          self.rect.center=self.rect_screen.center


    def dibujar_boton(self):
         self.screen.fill(self.button_color,self.rect)
         self.screen.blit(self.msg_image,self.msg_image_rect)
         #pygame.draw.rect(self.screen,self.button_color,self.rect)