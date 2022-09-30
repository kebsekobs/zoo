import random
import pygame
from pygame.locals import*
import os

pygame.init()
clock = pygame.time.Clock()
size = 700, 700
screen = pygame.display.set_mode(size)
board_units = [[[] * 10 for _ in range(10)] for i in range(10)]
new_board_units = board_units


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for k in range(self.height):
                pygame.draw.rect(screen, (0, 0, 0),
                                 ((self.left - self.cell_size) * i + self.left,
                                  (self.top - self.cell_size) * k + self.top, self.cell_size, self.cell_size), 1)


class Herbivorous(pygame.sprite.Sprite):
    image = load_image("rabbit.png")

    def __init__(self, group, x, y, power, kind):
        super().__init__(group)
        self.image = Herbivorous.image
        self.rect = self.image.get_rect()
        self.power = power
        self.kind = kind
        self.x = x * 50
        self.y = y * 50
        self.rect = self.rect.move(self.x, self.y)
        self.dead = False

    def update(self, x, y):
        self.rect = self.rect.move(x, y)
        print(self.rect)

    def die(self):
        self.dead = True


class BigPredator(pygame.sprite.Sprite):
    image = load_image("crocodile.png")

    def __init__(self, group, x, y, power, kind):
        super().__init__(group)
        self.image = BigPredator.image
        self.rect = self.image.get_rect()
        self.power = power
        self.kind = kind
        self.x = x * 50
        self.y = y * 50
        self.rect = self.rect.move(self.x, self.y)
        self.dead = False

    def update(self, x, y):
        self.rect = self.rect.move(x, y)

    def die(self):
        self.dead = True


class Predator(pygame.sprite.Sprite):
    image = load_image("dog.png")

    def __init__(self, group, x, y, power, kind):
        super().__init__(group)
        self.image = Predator.image
        self.rect = self.image.get_rect()
        self.power = power
        self.kind = kind
        self.x = x * 50
        self.y = y * 50
        self.rect = self.rect.move(self.x, self.y)
        self.dead = False

    def update(self, x, y):
        self.rect = self.rect.move(x, y)

    def die(self):
        self.dead = True


class Grass(pygame.sprite.Sprite):
    image = load_image("grass.png")

    def __init__(self, group, x, y, kind):
        super().__init__(group)
        self.image = Grass.image
        self.rect = self.image.get_rect()
        self.kind = kind
        self.x = x * 50
        self.y = y * 50
        self.rect = self.rect.move(self.x, self.y)

    def update(self, x, y):
        pass


herbivorous = pygame.sprite.Group()
big_predator = pygame.sprite.Group()
predator = pygame.sprite.Group()
grass = pygame.sprite.Group()
# for i in range(len(board_units)):
# for k in range(len(board_units[i])):
# if board_units[i][k][0] >= 1:
# Grass(grass, k + 2, i + 2)
# if board_units[i][k][1] >= 1:
# Herbivorous(herbivorous, k + 2, i + 2)
# if board_units[i][k][2] >= 1:
# Predator(predator, k + 2, i + 2)
# if board_units[i][k][3] >= 1:
# BigPredator(big_predator, k + 2, i + 2)
board = Board(10, 10)
board.set_view(100, 100, 50)
screen = pygame.display.set_mode((700, 700))
total = 0
running = True
for i in range(5):
    # power = random.randint(0, 400)
    power = 5
    kind = 'herbal'
    i = random.randint(0, 9)
    k = random.randint(0, 9)
    board_units[i][k].append(Herbivorous(herbivorous, k + 2, i + 2, power, kind))
    kind = 'grass'
    i = random.randint(0, 9)
    k = random.randint(0, 9)
    board_units[i][k].append(Grass(grass, k + 2, i + 2, kind))
    power = 100
    kind = 'predator'
    i = random.randint(0, 9)
    k = random.randint(0, 9)
    board_units[i][k].append(Predator(predator, k + 2, i + 2, power, kind))
    power = 200
    kind = 'big predator'
    i = random.randint(0, 9)
    k = random.randint(0, 9)
    board_units[i][k].append(BigPredator(big_predator, k + 2, i + 2, power, kind))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(board_units)
            new_board_units = [[[] * 10 for _ in range(10)] for i in range(10)]
            for i in range(len(board_units)):
                for k in range(len(board_units[i])):
                    for j in range(len(board_units[i][k])):
                        fight_big_predator = random.randint(0, 1)
                        # if i > 0 and i < 9 and k > 0 and k < 9:
                        if len(board_units[i][k]) > 0:
                            if board_units[i][k][j].kind == 'grass':
                                pass
                            elif board_units[i][k][j].kind == 'herbal':
                                for unit in range(len(board_units[i][k])):
                                    if board_units[i][k][unit].kind == 'grass':
                                        print(board_units[i][k][j].rect)
                                        board_units[i][k][unit].kill()
                            elif board_units[i][k][j].kind == 'predator':
                                for unit in range(len(board_units[i][k])):
                                    if board_units[i][k][unit].kind == 'herbal':
                                        # if board_units[i][k][j].power > board_units[i][k][unit].power:
                                        board_units[i][k][unit].die()
                                        board_units[i][k][unit].kill()
                            elif board_units[i][k][j].kind == 'big predator':
                                for unit in range(len(board_units[i][k])):
                                    if board_units[i][k][unit].kind == 'herbal' or board_units[i][k][unit].kind == 'predator':
                                        # if board_units[i][k][j].power > board_units[i][k][unit].power:
                                        board_units[i][k][unit].die()
                                        board_units[i][k][unit].kill()
                                    elif board_units[i][k][unit].kind == 'big predator':
                                        if fight_big_predator == 1:
                                            board_units[i][k][unit].power -= board_units[i][k][j].power / 2
                        new_position_x, new_position_y = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
                        if i == 9:
                            new_position_y = -1
                            new_position_x = 0
                        elif i == 0:
                            new_position_y = 1
                            new_position_x = 0
                        elif k == 9:
                            new_position_x = -1
                            new_position_y = 0
                        elif k == 0:
                            new_position_x = 1
                            new_position_y = 0
                        a1 = new_board_units[i + new_position_y][k + new_position_x]
                        a2 = board_units[i][k][j]
                        if a2.kind == 'grass':
                            new_board_units[i][k].append(a2)
                        elif not a2.dead:
                            a1.append(a2)
                        board_units[i][k][j].update(new_position_x * 50, new_position_y * 50)
                        total += 1
                        # Herbivorous(herbivorous, k + 2 + new_position_x, i + 2 + new_position_y)
                    # if board_units[i][k][1] >= 1:
                    # Herbivorous(herbivorous, k + 2, i + 2)
                # if board_units[i][k][2] >= 1:
                # Predator(predator, k + 2, i + 2)
                # if board_units[i][k][3] >= 1:
                # BigPredator(big_predator, k + 2, i + 2)
    board_units = new_board_units
    screen.fill((255, 255, 255))
    grass.draw(screen)
    herbivorous.draw(screen)
    predator.draw(screen)
    big_predator.draw(screen)
    board.render()
    pygame.display.flip()
