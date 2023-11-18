import pygame

# Colors
black = (0, 0, 0)
bright_green = (0, 255, 0)
green = (0, 200, 0)
red = (200, 0, 0)
bright_red = (255, 0, 0)
white = (255, 255, 255)


# Screen dimensions
width = 840
height = 650

# Initialize Pygame
pygame.init()

# Load assets
start = pygame.image.load("assets/start.png")
pygame.mixer_music.load("assets/music.mp3")
csound = pygame.mixer.Sound("assets/crash.wav")

# Clock
clock = pygame.time.Clock()

# Game window
gameD = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Dodge")

# Other variables
scroll = 0

imgroad = pygame.image.load("assets/background.png").convert_alpha()
carimg1 = pygame.image.load("assets/white_car.png").convert_alpha()
carimg2 = pygame.image.load("assets/blue_car.png").convert_alpha()
carimg3 = pygame.image.load("assets/pickup_truck.png").convert_alpha()
carimg4 = pygame.image.load("assets/bus.png").convert_alpha()
carimg5 = pygame.image.load("assets/semi_trailer.png").convert_alpha()
carimg6 = pygame.image.load("assets/police.png").convert_alpha()
red_car = pygame.image.load("assets/red_car.png").convert_alpha()
green_car = pygame.image.load("assets/green_car.png").convert_alpha()
crash = pygame.image.load("assets/crash.png")
crash_rect = crash.get_rect()
foo = [carimg1, carimg2, carimg3, carimg4, carimg5, carimg6]

lane_1 = 230
lane_2 = 360
lane_3 = 490
lane_4 = 620
lanes = [lane_1, lane_2, lane_3, lane_4]

# Player car initial position
player_x = lane_2
player_y = 550

pause = False
