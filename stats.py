class Stats:

    def __init__(self,settings):
        self.settings=settings
        self.reset_stats()
        self.juego_activo=False
        self.high_score=0
        self.high_level=1
        self.leer_high_score_level()
    

    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1


    def leer_high_score_level(self):
        filename='high score and high level.txt'
        try:
            with open(filename) as file_object:
                high_score=int(file_object.readline())
                high_level=int(file_object.readline())
            if high_score>self.high_score:
                self.high_score=high_score
            if high_level>self.high_level:
                self.high_level=high_level
        except (FileNotFoundError,ValueError):
            self.high_score=0
            self.high_level=1