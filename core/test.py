from core import colorz
from os import path
from time import time
import sys
import csv


def testTime(filename, size):
    start = time()
    colorz(filename, 6, size)
    finish = round(time() - start, 4)
    return finish
    
writer = csv.writer(open("some2.csv", "a", newline=''), dialect='excel')
filename = "8ed06e73048be838.jpg"

for i in range(10, 201):
    sys.stdout.write('\rРазмер изображения: {0} на {0} px'.format(i))
    #testName = sorted(list(colorz(filename, 6, (i,i))))
    test = [testTime(filename, (i,i)) for x in range(10)]
    sys.stdout.flush()
    #writer.writerow([i, testName, test])
    writer.writerow([i, test])