import pygame
from pygame.sprite import Sprite

# Classe que representa a nave
class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        # Inicializa a espaço nave e define sua posição inicial
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega o desenho da espaço nave na tela e obtém seu retângulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia a espaço nave no centro da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza a posição da espaço nave
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # Desenha a espaço nave em sua posição atual
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
