import pygame
import sys

class DevicesList:
    def __init__(self):
        self.devices = []
        self.currCoordX = 120
        self.currCoordY = 20
        self.coordYi = 50

    def addDevice(self):
        c = self.currCoordY
        self.currCoordY = self.currCoordY + self.coordYi
        return c


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

    def updateInfo(self, data):
        print("data -> ", data)
        if self.name == "U":
            self.name = data.split(":")[0]
        self.target_noise = min(int(float(data.split(":")[1])), self.max_noise)
        if self.target_noise < 20:
            self.bar_color = (0,255,0)
        elif self.target_noise < 50:
            self.bar_color = (220,220,0)
        else:
            self.bar_color = (255,0,0)

    def update(self, screen):
        self.basic_health(screen)

    def basic_health(self, screen):
        pygame.draw.rect(screen, self.bar_color, (self.coordX, self.coordY, self.target_noise / self.noise_ratio, 35))
        pygame.draw.rect(screen, (255, 255, 255), (self.coordX, self.coordY, self.noise_bar_length, 35), 4)
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(self.name, True, self.bar_color, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (self.coordX - 40, self.coordY + 20)
        screen.blit(text, textRect)

def updateScreen(screen, clock, deviceList):
    screen.fill((0, 0, 0))
    for dev in deviceList.devices:
        dev.update(screen)
    pygame.display.update()
    clock.tick(60)
"""
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


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
"""



# micro1 = pygame.sprite.GroupSingle(Micro(120, 20, "1"))
# startGame([micro1])
