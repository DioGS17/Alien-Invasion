# Classe com as configurações do jogo
class Settings():
    def __init__(self):
        # Configurações da tela
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Configurações da nave
        self.ship_limit = 3

        # Configurações de projéteis da nave
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Configurações do alien
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


        # Escala de aumento da velocidade do jogo
        self.speedup_scale = 1.1

        # Escala de aumeto de pontuação
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # Inicia as configurações dinâmicas
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # Pontuação
        self.aliens_points = 50

    # Aumenta a velocidade do jogo
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)