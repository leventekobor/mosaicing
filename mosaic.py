import cv2
import os
import random
import numpy as np
from matplotlib import pyplot as plt


def get_result_image(path):
    if(is_mosaic(path)):
        return demosaic(path)   
    else:
        return mosaic(path)
        

def demosaic(path):
    img = cv2.imread(path)
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
    path = path.replace(
    path.split(".")[len(path.split(".")) - 1], "png")
    cv2.imwrite(path, img)
    return path
                

def mosaic(path):
    img = cv2.imread(path)
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


def is_mosaic(path):
    img = cv2.imread(path)
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




