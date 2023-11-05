import random
from pygame.locals import *
from game_variable import *
from car import Vehicle, PlayerCar

vehicle_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player = PlayerCar(player_x, player_y)
player_group.add(player)


class Game:
    def __init__(self):

        self.width = width
        self.height = height
        self.gameD = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.green = green
        self.bright_green = bright_green
        self.red = red
        self.bright_red = bright_red
        self.black = black
        self.player_x = player_x
        self.player_y = player_y
        self.player = None
        self.gameplay = False
        self.pause = True
        self.high_scores = {}

    def game_intro(self):
        intro = True
        self.gameD.blit(start, (0, 0))
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            largeText = pygame.font.SysFont("comicsansms", 100)
            TextSurf, TextRect = self.text_objects("Race!", largeText)
            TextRect.center = (self.width / 2, self.height / 4)

            self.gameD.blit(TextSurf, TextRect)

            self.button("GO!", 200, 400, 100, 50, self.green, self.bright_green, self.choose_color)
            self.button("Quit", 600, 400, 100, 50, self.red, self.bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(60)

    def gameloop(self, speed):
        pygame.mixer.music.play(-1)
        gameexit = False
        previous_lane = None
        roady = 0
        roadyo = -650
        score = 0

        vehicle_group.empty()
        player.rect.center = (lane_2, 550)
        while not gameexit:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if player.rect.center[0] > lane_1:
                            player.rect.x -= 130
                        else:
                            crash_rect.center = [player.rect.center[0], player.rect.center[1]]
                            gameD.blit(crash, crash_rect)
                            self.crashed(score)
                    if event.key == K_RIGHT:
                        if player.rect.center[0] < lane_4:
                            player.rect.x += 130
                        else:
                            crash_rect.center = [player.rect.center[0], player.rect.center[1]]
                            gameD.blit(crash, crash_rect)
                            self.crashed(score)
                    if event.key == K_UP:
                        if player.rect.y > 0:
                            player.rect.y -= 100
                        else:
                            crash_rect.center = [player.rect.center[0], player.rect.center[1]]
                            gameD.blit(crash, crash_rect)
                            self.crashed(score)
                    if event.key == K_DOWN:
                        if player.rect.y < height - 100:
                            player.rect.y += 100
                        else:
                            crash_rect.center = [player.rect.center[0], player.rect.center[1]]
                            gameD.blit(crash, crash_rect)
                            self.crashed(score)
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.paused()
                    for vehicle in vehicle_group:
                        if pygame.sprite.collide_rect(player, vehicle):
                            crash_rect.center = [vehicle.rect.center[0], vehicle.rect.center[1]]
                            gameD.blit(crash, crash_rect)

                            self.crashed(score)

            if pygame.sprite.spritecollide(player, vehicle_group, True):
                crash_rect.center = [player.rect.center[0], player.rect.top]
                gameD.blit(crash, crash_rect)
                self.crashed(score)

            roady += speed
            if roady > height:
                roady = 0
                roadyo = -650

            if roady > 0:
                gameD.blit(imgroad, (0, roady))
                roadyo += speed
                self.road(roadyo)

            player_group.draw(gameD)

            if len(vehicle_group) < 3:
                add_vehicle = True
                for vehicle in vehicle_group:
                    if vehicle.rect.top < vehicle.rect.height * 2:
                        add_vehicle = False

                if add_vehicle:
                    lane = random.choice([lane for lane in lanes if lane != previous_lane])
                    image = random.choice(foo)
                    vehicle = Vehicle(image, lane, -50)
                    vehicle_group.add(vehicle)
                    previous_lane = lane
            for vehicle in vehicle_group:
                vehicle.rect.y += speed * 0.5
                if vehicle.rect.top >= height:
                    vehicle.kill()
                    score += 1
                    if score > 0 and score % 4 == 0:
                        speed += 1

            vehicle_group.draw(gameD)
            font = pygame.font.SysFont(None, 40)
            text = font.render("SCORE: " + str(score), True, black)
            gameD.blit(text, (0, 0))

            pygame.display.update()
            clock.tick(60)

    def choose_level(self):
        self.gameD.blit(start, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            largeText = pygame.font.SysFont("comicsansms", 100)
            TextSurf, TextRect = self.text_objects("Choose level", largeText)
            TextRect.center = (self.width / 2, self.height / 6)
            self.gameD.blit(TextSurf, TextRect)

            self.button("Beginer", 200, 300, 100, 50, self.green, self.bright_green, lambda: self.gameloop(4))
            self.button("Easy", 300, 300, 100, 50, self.green, self.bright_green, lambda: self.gameloop(6))
            self.button("Medium", 400, 300, 100, 50, self.green, self.bright_green, lambda: self.gameloop(8))
            self.button("Hard", 500, 300, 100, 50, self.green, self.bright_green, lambda: self.gameloop(16))
            self.button("Insane", 600, 300, 100, 50, self.green, self.bright_green, lambda: self.gameloop(20))

            pygame.display.update()
            self.clock.tick(60)

    def high_score(self):
        self.gameD.blit(start, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = self.text_objects("High Score", largeText)
        TextRect.center = (self.width / 2, self.height / 4)
        self.gameD.blit(TextSurf, TextRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Sort the high scores dictionary by score in descending order
            sorted_scores = sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True)

            # Display the top 5 scores
            y_pos = 220
            for i, (name, score) in enumerate(sorted_scores[:5], start=1):
                score_text = f"{i}. {name}: {score}"
                smallText = pygame.font.SysFont("comicsansms", 32)
                textSurf, textRect = self.text_objects(score_text, smallText)
                textRect.center = (self.width / 2, y_pos)
                self.gameD.blit(textSurf, textRect)
                y_pos += 50

            self.button("Play Again", 200, 500, 100, 50, self.green, self.bright_green, lambda: self.choose_level())
            self.button("Quit", 600, 500, 100, 50, self.red, self.bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(60)

    def crashed(self, score):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(csound)
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = self.text_objects("You Crashed", largeText)
        TextRect.center = (self.width / 2, self.height / 4)
        self.gameD.blit(TextSurf, TextRect)
        TextSurf, TextRect = self.text_objects("Enter your name", largeText)
        TextRect.center = (self.width / 2, self.height / 2.5)
        self.gameD.blit(TextSurf, TextRect)
        TextSurf, TextRect = self.text_objects("Press Enter", largeText)
        TextRect.center = (self.width / 2, self.height - 200)
        self.gameD.blit(TextSurf, TextRect)

        name = ""
        input_box = pygame.Rect(280, 350, 280, 60)
        color_inactive = pygame.Color(black)
        color_active = pygame.Color(white)
        color = color_inactive
        active = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            # Add the name and score to the dictionary
                            self.high_scores[name] = score
                            self.high_score()
                            return
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        elif len(name) < 12:
                            name += event.unicode
                    if event.key == pygame.K_KP_ENTER:
                        # Add the name and score to the dictionary
                        self.high_scores[name] = score
                        self.high_score()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive

            # Create a black box behind the input field
            pygame.draw.rect(self.gameD, black, input_box)

            txt_surface = pygame.font.Font(None, 50).render(name, True, color)
            self.gameD.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.gameD, color, input_box, 2)

            pygame.display.update()
            self.clock.tick(30)

    def paused(self):
        pygame.mixer.music.pause()
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = self.text_objects("Paused", largeText)
            TextRect.center = (self.width / 2, self.height / 2)
            self.gameD.blit(TextSurf, TextRect)

            self.button("Continue", 350, 450, 100, 50, self.green, self.bright_green, self.unpause)
            self.button("Quit", 900, 450, 100, 50, self.red, self.bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(60)

    def unpause(self):
        pygame.mixer.music.unpause()
        self.pause = False

    def choose_color(self):

        choose = True
        gameD.blit(start, (0, 0))
        while choose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            largeText = pygame.font.SysFont("comicsansms", 70)
            TextSurf, TextRect = self.text_objects("Choose your car color", largeText)
            TextRect.center = ((width / 2), (height / 4))

            gameD.blit(TextSurf, TextRect)

            gameD.blit(green_car, (220, 300))
            gameD.blit(red_car, (620, 300))
            self.button("Green Car", 200, 500, 100, 50, green, bright_green, lambda: self.set_color("green"))
            self.button("Red Car", 600, 500, 100, 50, red, bright_red, lambda: self.set_color("red"))

            pygame.display.update()
            clock.tick(60)

    def set_color(self, color):
        if color == "red":
            player.image = red_car
        elif color == "green":
            player.image = green_car
        self.choose_level()

    @staticmethod
    def quitgame():
        pygame.quit()
        quit()

    def text_objects(self, text, font):
        textsurface = font.render(text, True, self.black)
        return textsurface, textsurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.gameD, ac, (x, y, w, h))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.gameD, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x + (w / 2), y + (h / 2))
        self.gameD.blit(textSurf, textRect)

    def road(self, roady):
        self.gameD.blit(imgroad, (0, roady))
