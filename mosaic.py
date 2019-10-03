import cv2
import os


def create_mosaic(path):
    img = cv2.imread(path)
    rows = img.shape[0]
    cols = img.shape[1]
    blue = 0
    green = 0
    red = 0
    for i in range(rows):
        for j in range(cols):
            if(i % 2 != 0):
                if(j % 2 == 0):
                    img.itemset((i, j, 1), 0)
                    img.itemset((i, j, 2), 0)
                    blue += 1
                else:
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 2), 0)
                    green += 1
            else:
                if(j % 2 == 0):
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 2), 0)
                    green += 1
                else:
                    img.itemset((i, j, 0), 0)
                    img.itemset((i, j, 1), 0)
                    red += 1
    path = path.replace(
    path.split(".")[len(path.split(".")) - 1], "png")
    cv2.imwrite(path, img)
    return path
    
