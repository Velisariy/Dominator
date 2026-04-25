from collections import namedtuple
from math import sqrt
import colorsys
import numpy as np

try:
    import Image
except ImportError:
    from PIL import Image


def get_points(img):
    w, h = img.size
    result = img.getcolors(w * h)
    if result is None:
        result = img.convert('RGB').getcolors(w * h)
    counts = np.array([r[0] for r in result], dtype=np.float64)
    colors = np.array([r[1][:3] for r in result], dtype=np.float64)
    return colors, counts


def colorz(filename, n=3, size=(100, 100)):
    img = Image.open(filename)
    img.thumbnail(size)

    coords, counts = get_points(img)
    clusters = kmeans(coords, counts, n)
    rgbs = [c.tolist() for c in clusters]

    return rgbs


def kmeans(coords, counts, k):
    coords = np.asarray(coords)
    counts = np.asarray(counts)
    n_points = len(coords)

    indices = np.random.choice(n_points, k, replace=False)
    centers = coords[indices].copy()

    while True:
        distances = np.linalg.norm(coords[:, np.newaxis] - centers, axis=2)
        assignments = np.argmin(distances, axis=1)

        new_centers = np.zeros_like(centers)
        for i in range(k):
            mask = assignments == i
            if np.any(mask):
                total_counts = counts[mask].sum()
                weighted_sum = (coords[mask] * counts[mask, None]).sum(axis=0)
                new_centers[i] = weighted_sum / total_counts

        diff = np.max(np.linalg.norm(centers - new_centers, axis=1))
        centers = new_centers

        if diff < 1:
            break

    return np.round(centers).astype(int)


def lum(r, g, b):
    return sqrt(.241 * r + .691 * g + .068 * b)


def matching(color):
    '''
    Сравнение цвета со средним значением
    для читабельного отображения текста
    '''
    rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    luminance = colorsys.rgb_to_hls(*rgb)[1]

    if luminance > 180:
        return '#000000'
    else:
        return '#ffffff'
