import cv2
import os
import random


def get_result_image(path):
    img = cv2.imread(path)
    if(is_mosaic(img)):
        return mosaic(img)
    else:
        return demosaic(img)

def demosaic(img):
    green = 0
    blue = 0
    red = 0
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if(i % 2 == 0):
                if(img.item(i, j, 1) == 0):
                    img.itemset((i, j, 1),
                    (img.item(i, j - 1, 1) +
                    img.item(i, j + 1, 1) +
                    img.item(i - 1, j, 1) +
                    img.item(i + 1, j, 1)) / 4)
                if(img.item(i, j, 2) == 0):
                    if(j % 2 == 0):
                        img.itemset((i, j, 2),
                        (img.item(i - 1, j, 2) +
                        img.item(i + 1, j, 2) / 2))
                if(img.item(i, j, 0) == 0):
                    if(j % 2 == 0):
                        img.itemset((i, j, 0),
                        (img.item(i, j - 1, 0) +
                        img.item(i, j + 1, 0) / 2))
                    else:
                        img.itemset((i, j, 0),
                        (img.item(i - 1, j - 1, 0) +
                        img.item(i - 1, j + 1, 0) +
                        img.item(i + 1, j - 1, 0) +
                        img.item(i + 1, j + 1, 0)) / 4)
            else:
                if(img.item(i, j, 1) == 0):
                    img.itemset((i, j, 1),
                    (img.item(i, j - 1, 1) +
                    img.item(i, j + 1, 1) +
                    img.item(i - 1, j, 1) +
                    img.item(i + 1, j, 1)) / 4)
                if(img.item(i, j, 2) == 0):
                    if(j % 2 == 0):
                        img.itemset((i, j, 2),
                        (img.item(i - 1, j - 1, 2) +
                        img.item(i - 1, j + 1, 2) +
                        img.item(i + 1, j - 1, 2) +
                        img.item(i + 1, j + 1, 2)) / 4)
                    else:
                        img.itemset((i, j, 2),
                        (img.item(i - 1, j, 2) +
                        img.item(i + 1, j, 2) / 2))
                if(img.item(i, j, 0) == 0):
                    img.itemset((i, j, 0),
                    (img.item(i + 1, j, 0) +
                    img.item(i - 1, j, 0) / 2))

    cv2.imshow("demosaic", img)
    print(img)
    cv2.imwrite("done.png", img)
    cv2.waitKey(0)
                

def mosaic(img):
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            if(i % 2 != 0):
                if(j % 2 == 0):
                    img.itemset((i, j, 1), 0)
                    img.itemset((i, j, 2), 0)
                else:
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 2), 0)
            else:
                if(j % 2 == 0):
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 2), 0)
                else:
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 1), 0)
    path = path.replace(
    path.split(".")[len(path.split(".")) - 1], "png")
    cv2.imwrite(path, img)
    return path


def is_mosaic(img):
    for i in range(10):
        x = random.randint(0, img.shape[0])
        y = random.randint(0, img.shape[1])
        if (img.item(x, y, 0) == 0):
            if((img.item(x, y, 1) == 0 and img.item(x, y, 2) > 0) or
            (img.item(x, y, 1) > 0 and img.item(x, y, 2) == 0)):
                return True
        else:
            if(img.item(x, y, 0) > 0 and 
            img.item(x, y, 1) > 0 and
            img.item(x, y, 2) > 0):
                return False


img = cv2.imread("/Users/mac/Documents/greenfox/mosaicing/static/img/parrot-super-web-page.png")
demosaic(img)