# coding: UTF-8

import sys
from time import time
from core import core, design
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread

try:
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.colors import HexColor

    pdf = False
except ImportError:
    pdf = False


class ImageCollector(QThread):
    def __init__(self, filename: str, count: int):
        super().__init__()

        self.filename = filename
        self.count = count
        self.colors = []

    def __del__(self):
        self.wait()

    def run(self):
        self.colors = list(core.colorz(self.filename, self.count))


class MainProgram(design.MainWindow):
    """
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    """

    def __init__(self):
        super().__init__()

        self.openImage.triggered.connect(self.showDialog)
        self.saveImage.triggered.connect(self.saveDialog)
        self.refreshImageAction.triggered.connect(self.refreshImage)

    def _procImageDone(self):
        # Определяем список доминирующих цветов
        self.colors = self.colors_thread.colors
        self.colors.sort()

        # Загружаем изображение и редактируем его
        pix = QtGui.QPixmap()
        pix.load(self.filename)
        w = float(pix.width())
        h = float(pix.height())
        k = round(w / h, 2)
        self.imgLabel.setPixmap(pix.scaled(600 * k, 600))

        self.colorsLayout(self.colors)

        self.statusBar().showMessage("Выполнено за {} сек.".format(round(time() - self.start, 3)))

        self.refreshImageAction.setDisabled(False)

    def procImage(self, filename: str):
        self.refreshImageAction.setDisabled(True)
        self.start = time()
        self.filename = filename

        self.colors_thread = ImageCollector(filename, self.spinBox.value())
        self.colors_thread.finished.connect(self._procImageDone)
        self.colors_thread.start()

    def saveDialog(self):
        if not pdf:
            return self.message('Не установлена библиотека reportlab')

        file = QtWidgets.QFileDialog.getSaveFileName(caption="Сохранить изображение", filter="*.pdf")[0]

        if file and pdf:
            self.savePdf(file)

    def showDialog(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(caption="Открыть изображение")[0]
        if self.filename:
            self.refreshImageAction.setDisabled(False)
            self.saveImage.setDisabled(False)
            self.procImage(self.filename)

    def savePdf(self, file: str):
        colors = self.colors
        imgfile = self.filename
        canvas = Canvas(file, pagesize=A4)
        pdfmetrics.registerFont(TTFont('Arial', 'font/Arial.ttf'))
        canvas.setFont('Arial', 16)
        canvas.drawString(20, 800, "Доминирующие цвета")
        canvas.setFont('Arial', 12)
        for key, color in enumerate(colors):
            canvas.setFillColor(HexColor('#%s' % color))
            canvas.rect(20, 765 - 30 * key, 70, 25, fill=1, stroke=0)

            canvas.setFillColor(HexColor(core.matching(color)))
            canvas.drawCentredString(50, 775 - 30 * key, '#{}'.format(color))

            canvas.drawImage(imgfile, 100, 390, 300, 400, preserveAspectRatio=True, anchor='nw')

        canvas.save()

    def refreshImage(self):
        self.procImage(self.filename)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
