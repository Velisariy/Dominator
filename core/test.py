from core import colorz
from os import path
from time import time
import sys
import csv


def testTime(size):
    start = time()
    colorz("c:/Разобрать/anime-817437.jpeg", 6, size)
    finish = round(time() - start, 4)
    return finish
    
writer = csv.writer(open("some.csv", "a", newline=''), dialect='excel')
for i in range(200, 201):
    sys.stdout.write('\rРазмер изображения: {0} на {0} px'.format(i))
    testName = sorted(list(colorz("c:/Разобрать/anime-817437.jpeg", 6, (i,i))))
    test = [testTime((i,i)) for x in range(10)]
    sys.stdout.flush()
    writer.writerow([i, testName, test])