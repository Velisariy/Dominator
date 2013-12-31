from core import colorz
from os import path
import time
import queue


start = time.time()
que = queue.Queue()
va = colorz("c:/Разобрать/anime-817437.jpeg", 6, que)
print (list(que.get()))
print ('time: %f' % (time.time() - start))