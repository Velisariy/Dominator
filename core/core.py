# -*-coding: utf-8 -*-
from collections import namedtuple
from math import sqrt
import random
import colorsys

try:
    import Image
except ImportError:
    from PIL import Image

Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))


def get_points(img):
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    return points


def colorz(filename, n=3, size=(100, 100)):
    img = Image.open(filename)
    img.thumbnail(size)

    points = get_points(img)
    clusters = kmeans(points, n, 1)
    rgbs = [list(map(int, c.center.coords)) for c in clusters]

    return rgbs


def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))


def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)


def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters


def lum(r, g, b):
    return sqrt(.241 * r + .691 * g + .068 * b)


def matching(color):
    '''
    Сравнение цвета со средним значением
    для читабельного отображения текста
    '''
    color.strip('#')
    rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    luminance = colorsys.rgb_to_hls(*rgb)[1]

    if luminance > 180:
        result = "black"
    else:
        result = "white"

    return result
