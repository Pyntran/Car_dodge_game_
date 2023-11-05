import pygame
from game import Game

pygame.init()

if __name__ == "__main__":
    game = Game()
    game.game_intro()
    pygame.quit()
