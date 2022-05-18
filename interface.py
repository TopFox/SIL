import pygame
import sys


class DevicesList:
    def __init__(self):
        self.devices = []
        self.currCoordX = 120
        self.currCoordY = 20
        self.coordYi = 50

    def addDevice(self):
        self.devices.append(pygame.sprite.GroupSingle(Micro(self.currCoordX, self.currCoordY)))
        self.currCoordY = self.currCoordY + self.coordYi


class Micro(pygame.sprite.Sprite):

    def __init__(self, coordX, coordY):
        super().__init__()
        self.coordX = coordX
        self.coordY = coordY
        self.name = "U"
        self.bar_color = (255, 0, 0)
        self.target_noise = 50
        self.max_noise = 100
        self.noise_bar_length = 600
        self.noise_ratio = self.max_noise / self.noise_bar_length
        self.health_change_speed = 5

    def update(self):
        self.basic_health()

    def basic_health(self):
        pygame.draw.rect(screen, self.bar_color, (self.coordX, self.coordY, self.target_noise / self.noise_ratio, 35))
        pygame.draw.rect(screen, (255, 255, 255), (self.coordX, self.coordY, self.noise_bar_length, 35), 4)


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def startGame():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

        screen.fill((30, 30, 30))
        for dev in deviceList.devices:
            dev.update()
        pygame.display.update()
        clock.tick(60)


deviceList = DevicesList()

# micro1 = pygame.sprite.GroupSingle(Micro(120, 20, "1"))
# startGame([micro1])
