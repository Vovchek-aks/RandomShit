from PIL import Image, ImageDraw


def vec_sum(*args: tuple):
    return tuple(sum((args[j][i] for j in range(len(args)))) for i in range(len(args[0])))


def vec_mul(vec1: tuple, n: float):
    return vec1[0] * n, vec1[1] * n


def vec_mul_mat(vec: tuple, mat: tuple):
    return vec_sum(vec_mul((mat[0][0], mat[1][0]), vec[0]),
                   vec_mul((mat[0][1], mat[1][1]), vec[1]))


im1 = Image.open('data/test.jpg')
pixels1 = im1.load()

size = im1.size
print(size)

im2 = Image.new('RGB', size, 0)
pixels2 = im2.load()

# ij = ((1, 0),
#       (0, 1))
ij = ((1, 0.25),
      (.1, 0.4))

for x in range(size[0]):
    for y in range(size[1]):
        c = pixels1[x, y]

        x1, y1 = vec_mul_mat((x - size[0] / 2, -y + size[1] / 2), ij)
        x1 = round(x1) + size[0] / 2
        y1 = -round(y1) + size[1] / 2
        # print(x, y, 0 <= x1 < size[0], 0 <= y1 < size[1])
        if 0 <= x1 < size[0] and 0 <= y1 < size[1]:
            pixels2[x1, y1] = c


Image._show(im2)
im2.save(f'data/{str(ij)}.jpg')

