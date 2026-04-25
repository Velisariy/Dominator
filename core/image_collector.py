from math import sqrt
import colorsys
from PyQt6.QtCore import QThread
from core.core import colorz


class ImageCollector(QThread):
    """Параллельный тред для вычисления доминирующих цветов."""
    
    def __init__(self, filename: str, count: int):
        super().__init__()

        self.filename = filename
        self.count = count
        self.colors = []

    def __del__(self):
        self.wait()

    def run(self):
        """Вычисление доминирующих цветов в отдельном потоке."""
        # Получаем список доминирующих цветов
        self.colors = list(colorz(self.filename, self.count))
        
        # Сортируем по светлоте для читабельного отображения текста
        self.colors.sort(key=lambda rgb: self.sort(*rgb, 8))

    def sort(self, r, g, b, repetitions=1):
        """Сортировка цветов по светлоте с учётом повторений."""
        lum_val = self.lum(r, g, b)

        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        h2 = int(h * repetitions)
        lum2 = int(lum_val * repetitions)
        v2 = int(v * repetitions)

        if h2 % 2 == 1:
            v2 = repetitions - v2
            lum2 = repetitions - lum2
        return h2, lum2, v2

    def lum(self, r, g, b):
        return sqrt(.241 * r + .691 * g + .068 * b)
