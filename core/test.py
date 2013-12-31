from core import colorz
from os import path
import time

start = time.time()
va = colorz("c:/Разобрать/anime-817437.jpeg", 6)
print (list(va))
print ('time: %f' % (time.time() - start))