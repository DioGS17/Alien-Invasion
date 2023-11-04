import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    # Inicializa o jogo
    pygame.init()

    # Cria a tela
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(screen, ai_settings)  # Cria a nave
    bullets = Group()                 # Cria um grupo de projéteis
    aliens = Group()                  # Cria um grupo de aliens

    # Cria o alien
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria o botão de play
    play_button = Button(ai_settings, screen, "Play")

    # Laço principal do jogo
    while True:
        # Laço de eventos
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Movimento da nave
            ship.update()

            # Controle de projéteis
            gf.update_bullet(ai_settings, screen, stats, sb , ship, aliens, bullets)

            # Atualiza os aliens
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        # Mostra a tela mais recente
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)

run_game()
