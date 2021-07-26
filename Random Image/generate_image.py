from PIL import Image, ImageDraw
from random import randint


def sr_color(*args: tuple) -> tuple:
    res = [0, 0, 0]
    for i in args:
        for j in range(len(i)):
            res[j] += i[j]

    for i in range(len(res)):
        res[i] /= len(args)
        res[i] = round(res[i])

    return tuple(res)


def distance(a: tuple, b: tuple) -> float:
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])

    return (dx**2 + dy**2)**0.5


size = (1000, 1000)

m_dist = (distance((0, 0), size)) ** 0.5

image = Image.new('RGB', size, color=(255, 255, 255))
drawer = ImageDraw.ImageDraw(image)
pixels = image.load()

dots = []

err = 0
for x in range(size[0]):
    for y in range(size[1]):
        dist = (distance((size[0] // 2, size[1] // 2), (x, y))) ** 0.5

        if dist == 0:
            dist = 0.0000001

        color = 255 - round((dist / m_dist) * 255)

        pixels[x, y] = sr_color((color, color, color), tuple(randint(0, 255) for i in range(3)))
        # pixels[x, y] = (color, color, color)

    if not x % 100:
        print(x)


image.save('Test.png')


