import pygame
import random
import time


start_time = time.time()
pygame.init()

win_dim = 800
win = pygame.display.set_mode((win_dim, win_dim))


class Char:

    def __init__(self):

        self.x = 400
        self.y = 400
        self.dim = 20
        self.vsp = 0
        self.yeetdist = 0
        self.population = 0
        self.STime = 0  # Time of survival

    def draw_char(self, color):

        pygame.draw.rect(win, (color[0], color[1], color[2]), (self.x, self.y, self.dim, self.dim))

    def jump(self, bool):

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE] or bool == True) and self.y == 400:
            self.vsp = 5

        self.y -= self.vsp

        if self.y < 400:
            self.vsp -= 0.15
        else:
            self.y = 400

    def generateRnd(self):

        if ranGen == 0:
            self.population = round(random.random(), 5)
            print(self.population, "This is pop")

        else:
            self.population = times[-1][1] + (random.randint(-1, 1) / 10)
            pass



    def jumpval(self):

        if abs(self.yeetdist - self.population) < 0.005:
            return True

    def timer(self, x):

        # Code to add time

        self.STime += 1


class Cactus:

    def __init__(self, dim):

        self.dim = dim

        self.cac = []
        self.speed = 0


    def startcac(self, x):

        if x % 100 == 0:

            stop_time = time.time()
            self.cac.append(801)


        for i in range(0, len(self.cac)):

            if self.speed < 4:
                self.speed = 1 + x * 0.0005
            else:
                self.speed == 10

            self.cac[i] -= self.speed
            pygame.draw.rect(win, (0, 200, 0), (self.cac[i], 400, 20, 20))

        try:
            if self.cac[0] < 0:
                self.cac.pop(0)
        except IndexError:
            pass


    def collision(self, blob_cords):

        if any(i in [int(i) for i in self.cac] for i in [i for i in range(380, 421)]) and blob_cords[1] >= 380:
            return True

            # Here be sex and kill time

        yeetdist = 0

        if len(self.cac) >= 2:
            for i in self.cac:
                if i > 400 + 20:
                    yeetdist = (i - 400 - 20) / (self.cac[-1] - self.cac[-2])

                    break

        if yeetdist <= 1:
            # print(yeetdist, "Infam yeet")
            for items in AIs:
                items.yeetdist = yeetdist
            # print(self.speed / 4)

ranGen = 0

while True:

    AIs = []

    for i in range(10):
        AIs.append(Char())

    for obj in AIs:
        obj.generateRnd()

    cact = Cactus(20)

    x = 1
    times = []

    if __name__ == '__main__':

        game = True
        while game:
            pygame.time.delay(1)
            keys = pygame.key.get_pressed()


            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_s]:
                    game = False

            # Draws things on screen

            win.fill((0, 0, 0))
            for obj in AIs:
                obj.draw_char([150, 0, 0])
                obj.jump(obj.jumpval())


            # blob.jump(False)
            # blob.draw_char([150, 0, 0])

            for obj in AIs:
                obj.timer(x)
            cact.startcac(x)
            x += 1

            for obj in AIs:


                if cact.collision((obj.x, obj.y)) == True:
                    times.append((obj.STime, obj.population))
                    AIs.remove(obj)

            print(len(AIs))
            if len(AIs) < 1:
                game = False
            # cact.collision((blob.x, blob.y))

            # Updates movements and events


            # Update display

            pygame.display.update()

        for obj in AIs:
            times.append((obj.STime, obj.population))
        print(times)
        print(times.sort())

    ranGen = 1




pygame.QUIT()

