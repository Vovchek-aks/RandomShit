import pygame as pg
import os


class Wind:
    def __init__(self, sz, scl):
        self.sz = sz
        self.size = sz[0] * scl, sz[1] * scl
        self.pos = [(sz[i] - self.size[i]) / 2 for i in [0, 1]]
        self.arr_pos = [0, 0]
        self.realPos = [0, 0]

    def draw(self):
        pg.draw.rect(sc, (255, 0, 0), (*self.pos, *self.size), 1)
        # if 0 < self.arr_pos[0] < self.size[0] and \
        #    0 < self.arr_pos[1] < self.size[1]:
        sc.blit(im, self.realPos)

    def update(self, pos):
        self.arr_pos = [(self.size[i] / self.sz[i]) * pos[i] for i in [0, 1]]
        self.realPos = [self.arr_pos[i] + self.pos[i] for i in [0, 1]]


def load_image(name, colorkey=None):  # загружает картинки
    fullname = os.path.join('DE_data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit(0)
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


size = width, height = 1200, 800

pg.init()
sc = pg.display.set_mode(size)

im = pg.transform.scale(load_image('cursor.png'), (16, 16))

pg.display.set_caption('discord')

clock = pg.time.Clock()

font = pg.font.Font(None, 24)
font2 = pg.font.Font(None, 48)

w = Wind(size, 0.9)

while True:
    sc.fill((50, 50, 70))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)

        elif event.type == pg.MOUSEMOTION:
            w.update(event.pos)

    # sc.blit(font.render(str(round(clock.get_fps())), False, red), (width - 50, 30))

    w.draw()

    pg.display.flip()
    clock.tick(60)





