class Settings:
    def __init__(self):
        self.screen_width=1000
        self.screen_height=600
        self.background_color=230,230,230

        '''
        Configuraciones de los bullets
        '''
        self.bullet_factor_velocidad=3
        self.bullet_width=15
        self.bullet_height=400
        self.bullet_color=0,0,255
        self.bullet_permitidos=3


        self.fleet_speed_down=4
        self.fleet_direccion=1
        self.ship_limit=3
        self.speed_up_game=1.1
        
        self.inicia_dinamic_settings()

        self.alien_points=50
        self.score_escala=1.5

    def inicia_dinamic_settings(self):
        self.ship_speed_factor=0.5
        self.bullet_speed_factor=1
        self.alien_speed_factor=0.5

    def incrementa_speed(self):
        self.ship_speed_factor=self.ship_speed_factor*self.speed_up_game
        self.bullet_speed_factor*=self.speed_up_game
        self.alien_speed_factor*=self.speed_up_game
        self.alien_points=int(self.alien_points*self.score_escala)