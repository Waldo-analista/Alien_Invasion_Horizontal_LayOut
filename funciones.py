import pygame
import sys
from bullet import Bullet
from alien import Alien

from time import sleep

def check_eventos(screen,settings,ship,bullets,aliens,stats,boton_play):
    '''
    Función que chequea eventos
    '''
    for event in pygame.event.get():  #lista con los eventos
        if event.type==pygame.QUIT:
            sys.exit()    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ship.up_move=True
            if event.key==pygame.K_DOWN:
                ship.down_move=True   
            if event.key==pygame.K_SPACE:
                if len(bullets)<settings.bullet_permitidos:
                    sonido_bullet(stats)
                    new_bullet=Bullet(settings,screen,ship)
                    bullets.add(new_bullet)    
            if event.key==pygame.K_s:
                    stats.juego_activo=True
                    reset_juego(screen,settings,ship,bullets,aliens,stats)                                               
        if event.type==pygame.KEYUP:            
            if event.key==pygame.K_UP:
                ship.up_move=False
            if event.key==pygame.K_DOWN:
                ship.down_move=False
            if event.key==pygame.K_q:
                sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if not stats.juego_activo:
                if boton_play.rect.collidepoint(mouse_x,mouse_y):
                    stats.juego_activo=True
                    reset_juego(screen,settings,ship,bullets,aliens,stats)

def sonido_bullet(stats):
    if stats.juego_activo:
        pygame.mixer.Sound('laser.wav').play()

def actualiza_screen(screen,settings,ship,bullets,aliens,stats,boton_play,tablero):
    '''
    Función que actualiza la pantalla.Se llama en el ciclo while
    '''
    screen.fill(settings.background_color)    
    ship.dibujar_ship()
    aliens.draw(screen)
    tablero.show_score()  
    if stats.juego_activo:
        aliens.update()
        check_bordes(settings,aliens)

        for bullet in bullets.sprites():
            bullet.dibujar_bullet()
        bullets.update()

        for bullet in bullets.copy().sprites():
            if bullet.rect.right>=settings.screen_width:
                bullets.remove(bullet)
    
        colision=pygame.sprite.groupcollide(bullets,aliens,False,True) 
        if colision:
            for aliens1 in colision.values():
                stats.score+=settings.alien_points*len(aliens1)
                tablero.show_score()
                check_high_score(stats)

        if len(aliens)==0:
            crear_flota(settings,screen,ship,aliens)
            bullets.empty()  
            settings.incrementa_speed()
            stats.level+=1
            check_high_level(stats)
        
        if pygame.sprite.spritecollideany(ship,aliens):
            ship_hit(screen,settings,ship,bullets,aliens,stats)


        check_aliens_bottom(screen,settings,ship,bullets,aliens,stats)
        ship.mov_continuo()
    else:
        boton_play.dibujar_boton()

    pygame.display.flip()  



def crear_flota(settings,screen,ship,aliens):
    alien=Alien(settings,screen)#se crea un objeto alien para obtener sus datos de ancho
    alien_width=alien.rect.width
    alien_height=alien.rect.height

    espacio_disponible_y=settings.screen_height-2*alien_height
    numero_aliens_y=espacio_disponible_y//(2*alien_height)

    espacio_disponible_x=settings.screen_width-ship.rect.width-3*alien.rect.width
    numero_columnas=espacio_disponible_x//(2*alien_width)

    for column in range(numero_columnas):
        for alien_number in range(numero_aliens_y):
            alien=Alien(settings,screen)

            alien.y=alien_height+2*alien_height*alien_number
            alien.x=settings.screen_width-(2*alien_width+2*alien_width*column)
            alien.rect.y=alien.y
            alien.rect.x=alien.x
            aliens.add(alien)




def cambiar_direccion_flota(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.x-=settings.fleet_speed_down
    settings.fleet_direccion*=-1

def check_bordes(settings,aliens):#funcion cambia direccion de la flota al chequear bordes
    for alien in aliens.sprites():
        if alien.rect.bottom>=settings.screen_height or alien.rect.top<=0:
            cambiar_direccion_flota(settings,aliens)
            break






def ship_hit(screen,settings,ship,bullets,aliens,stats):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        crear_flota(settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.juego_activo=False
        pygame.mouse.set_visible(True)
        escribir_high_score_level(stats)




def check_aliens_bottom(screen,settings,ship,bullets,aliens,stats):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left<=screen_rect.left:
            ship_hit(screen,settings,ship,bullets,aliens,stats)
            break


def reset_juego(screen,settings,ship,bullets,aliens,stats):
    stats.reset_stats()
    aliens.empty()
    bullets.empty()
    crear_flota(settings,screen,ship,aliens)
    ship.center_ship()
    pygame.mouse.set_visible(False)
    settings.inicia_dinamic_settings()


def check_high_score(stats):
    if stats.score>stats.high_score:
        stats.high_score=stats.score

def check_high_level(stats):
    if stats.level>stats.high_level:
        stats.high_level=stats.level


def escribir_high_score_level(stats):
    filename='high score and high level.txt'
    high_score,high_level=leer_file()
    with open(filename,'w') as file_object:
        if stats.high_score>high_score:
            file_object.write(str(stats.high_score)+'\n')
        else:
            file_object.write(str(high_score)+'\n')
        if stats.high_level>high_level:
            file_object.write(str(stats.high_level))
        else:
            file_object.write(str(high_level))
            
def leer_file():
    filename='high score and high level.txt'   
    try:
        with open(filename,'r') as file_object:  
            high_score=int(file_object.readline())
            high_level=int(file_object.readline())  
        return  high_score,high_level
    except:
        return 0,1   