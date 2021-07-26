import pygame as pg
import os


class Wind:
    def __init__(self, sz, scl):
        self.sz = sz
        self.size = sz[0] * scl, sz[1] * scl
        self.pos = [(sz[i] - self.size[i]) / 2 for i in [0, 1]]
        self.arr_pos = [0, 0]
        self.realPos = [0, 0]

    def draw(self, pos):
        pos = [pos[i] + self.pos[i] for i in [0, 1]]
        pg.draw.rect(sc, (255, 0, 0), (*pos, *self.size), 1)
        # if 0 < self.arr_pos[0] < self.size[0] and \
        #    0 < self.arr_pos[1] < self.size[1]:
        sc.blit(im, self.realPos)

    def update(self, pos, d=(0, 0)):
        self.arr_pos = [(self.size[i] / self.sz[i]) * pos[i] for i in [0, 1]]
        self.arr_pos = [self.arr_pos[j] + d[j] for j in [0, 1]]
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

ws = []
s = size
scale = 0.8
for i in range(5):
    w = Wind(s, scale)
    s = [s[j] * scale for j in [0, 1]]
    ws += [w]


while True:
    sc.fill((50, 50, 70))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)

        elif event.type == pg.MOUSEMOTION:
            ws[0].update(event.pos)
            for i in range(1, len(ws)):
                # ws[i].update([event.pos[j] * (1 + scale**i) for j in [0, 1]])
                ws[i].update(ws[i - 1].realPos)

    # sc.blit(font.render(str(round(clock.get_fps())), False, red), (width - 50, 30))
    pos = (0, 0)
    for i in ws:
        i.draw(pos)
        pos = [pos[j] + i.pos[j] for j in [0, 1]]
        # print(pos)

    # exit()
    #
    # for i in range(len(ws[1:])):
    #     ws[i].update(ws[i-1].arr_pos)

    pg.display.flip()
    clock.tick(60)





