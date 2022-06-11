from PIL import Image


def color_dist(c1, c2):
    return ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)**.5


colors = [
    (255, 0, 0),        # red
    (128, 0, 0),        # d_red
    (0, 255, 0),        # green
    (0, 128, 0),        # d_green
    (0, 0, 255),        # blue
    (0, 0, 128),        # d_blue
    (0, 0, 0),          # black
    (128, 128, 128),    # gray
    (200, 200, 200),    # gray 2
    (20, 20, 20),       # gray 3
    (230, 230, 230),    # white
    (150, 80, 128),     # pink
    (130, 100, 130),    # pink 2
    (180, 128, 50),     # orange
    (200, 160, 100),    # orange 2
    (150, 80, 10),    # orange 3
    (149, 102, 82),    # orange 3
    (160, 140, 100),    # body
    (246, 216, 119),    # body 2
    (116, 76, 77),    # body 3
    (167, 137, 137),    # body 4
]


im = Image.open('data/test.jpg')
im = im.resize((100, 100), Image.BOX)

# Image._show(im)
im.save('data/test2.png')

pixels = im.load()
x, y = im.size

for i in range(x):
    for j in range(y):
        pixels[i, j] = min(map(lambda x: (x, color_dist(x, pixels[i, j])), colors), key=lambda x: x[1])[0]


im.save('data/test3.png')








