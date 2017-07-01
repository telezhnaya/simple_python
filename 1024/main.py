import cv2
import numpy as np

from random import choice, randrange
w = 1920
h = 1080

once = 32
quart = 8

for num in range(once):
    channels = []

    for i in range(3):
        channels.append(np.empty([h, w]))
        channels[i].fill(randrange(256))

    img = cv2.merge(channels)

    text = '1024'

    fontFace = choice([cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_COMPLEX])
    fontScale = 15
    thickness = 60

    color = (randrange(256), randrange(256), randrange(256))

    (tw, th), _ = cv2.getTextSize(text, fontFace, fontScale, thickness)
    pos = ((w - tw) // 2, (h + th) // 2)

    cv2.putText(img, text, pos, fontFace, fontScale, color, thickness)


    cv2.imwrite(str(num) + '.png', img)


def join_vert(start, stop):
    print(start, stop)
    img1 = cv2.imread(str(randrange(start, stop)) + '.png')
    img2 = cv2.imread(str(randrange(start, stop)) + '.png')
    return np.concatenate((img1, img2), axis=0)


def join_imgs(start, stop):
    vert1 = join_vert(start, stop)
    vert2 = join_vert(start, stop)
    res = np.concatenate((vert1, vert2), axis=1)
    return cv2.resize(res, (w, h))


for num in range(once, once + quart):
    res = join_imgs(0, once)
    cv2.imwrite(str(num) + '.png', res)

final = join_imgs(once, once + quart)
cv2.imwrite('final.png', final)


