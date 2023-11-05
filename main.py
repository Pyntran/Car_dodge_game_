import pygame
from Car_dodge_game.game import Game

pygame.init()

if __name__ == "__main__":
    game = Game()
    game.game_intro()
    pygame.quit()
