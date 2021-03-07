import json
from PIL import ImageColor
from random import randrange
from math import sqrt
import random


def main():
    global vectors
    data = json.load(open('xkcd.json',))
    vectors = processData(data)
    # print(vectors)
    global pos
    # pos = (255, 0, 0)
    rrr = getColor("R: ")
    ggg = getColor("G: ")
    bbb = getColor("B: ")

    pos = (rrr, ggg, bbb)
    nrstClr = findNearest(pos, vectors)
    print(
        f"The nearest color to ({rrr}, {ggg}, {bbb}) is '{nrstClr[0]}' {nrstClr[1]}")
    # for i in range(12):
    #     pos = (255, i*10, i*10)
    #     rednames = findNearest(pos, vectors)
    #     pos = (i*10, i*10, 255)
    #     bluenames = findNearest(pos, vectors)
    #     print("Roses are " + rednames + ", violets are " + bluenames)
    # red = vectors[random.choice(rednames[1:])]
    # blue = vectors[random.choice(bluenames[1:])]


def processData(data):
    vectors = {}
    colors = data["colors"]
    for i in range(len(colors)):
        label = colors[i]["color"]
        rgb = colors[i]["hex"]
        vectors[label] = (ImageColor.getcolor(str(rgb), "RGB"))
    return(vectors)


def findNearest(v, vectors):

    keys = list(vectors.keys())
    keys = sorted(keys, key=distance)
    # print(v)
    print(vectors[keys[0]])

    return keys[0], vectors[keys[0]]


def distance(x):
    return (distanceBetween(x, pos))


def distanceBetween(x, y):
    x = vectors[x]
    xx = int(x[0])
    xxx = int(y[0])
    yy = int(x[1])
    yyy = int(y[1])
    zz = int(x[2])
    zzz = int(y[2])
    answer = sqrt((xx - xxx) ** 2 + (yy - yyy) ** 2 + (zz - zzz) ** 2)
    return answer


def getColor(prnted):
    clrInput = input(prnted)
    if not clrInput.isdigit():
        ccllrr = getColor(prnted)
        ccllrr = int(ccllrr)
    else:
        ccllrr = int(clrInput)
    if ccllrr < 0 or ccllrr > 256:
        ccllrr = getColor(prnted)
    return ccllrr


if __name__ == '__main__':
    main()
