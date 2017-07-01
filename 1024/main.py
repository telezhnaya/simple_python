import cv2
import numpy as np

from random import choice, randrange
w = 1920
h = 1080

once = 32
quart = 8

hues = np.linspace(0, 180, once, endpoint=False)
np.random.shuffle(hues)

for num in range(once):
    channels = []

    color = (hues[num], randrange(128) + 128, randrange(128) + 128)
    color = cv2.cvtColor(np.array([[color]], np.uint8), cv2.COLOR_HSV2RGB)[0][0]
    for i in range(3):
        channels.append(np.empty([h, w]))
        channels[i].fill(color[i])

    img = cv2.merge(channels)

    text = '1024'

    fontFace = choice([cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_COMPLEX])
    fontScale = 15
    thickness = 60

    textColor = cv2.cvtColor(np.array([[color]], np.uint8), cv2.COLOR_RGB2HSV)[0][0]
    textColor[0] = (textColor[0] + 90) % 180
    textColor[1] = 255
    textColor[2] = 255
    textColor = cv2.cvtColor(np.array([[textColor]], np.uint8), cv2.COLOR_HSV2RGB)[0][0]

    (tw, th), _ = cv2.getTextSize(text, fontFace, fontScale, thickness)
    pos = ((w - tw) // 2, (h + th) // 2)

    cv2.putText(img, text, pos, fontFace, fontScale, tuple(map(int, textColor)), thickness)


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

