# coding: UTF-8

import sys
from time import time
from core import core, design
from PyQt5 import QtWidgets, QtGui

try:
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.colors import HexColor

    pdf = False
except ImportError:
    pdf = False


class MainProgram(design.MainWindow):
    """
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    """

    def __init__(self):
        super().__init__()

        self.openImage.triggered.connect(self.showDialog)
        self.saveImage.triggered.connect(self.saveDialog)
        self.refreshImageAction.triggered.connect(self.refreshImage)

    def procImage(self, filename):
        start = time()

        # Определяем список доминирующих цветов
        self.colors = list(core.colorz(filename, self.spinBox.value()))
        self.colors.sort()

        # Загружаем изображение и редактируем его
        pix = QtGui.QPixmap()
        pix.load(filename)
        w = float(pix.width())
        h = float(pix.height())
        k = round(w / h, 2)
        self.imgLabel.setPixmap(pix.scaled(600 * k, 600))

        self.colorsLayout(self.colors)

        self.statusBar().showMessage(u"Выполнено за {} сек.".format(round(time() - start, 3)))


    def saveDialog(self):
        if not pdf:
            return self.message('Не установлена библиотека reportlab')

        file = QtWidgets.QFileDialog.getSaveFileName(caption="Сохранить изображение", filter="*.pdf")[0]

        if file and pdf:
            self.savePdf(file)

    def showDialog(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(caption=u"Открыть изображение")[0]
        if self.filename:
            self.refreshImageAction.setDisabled(False)
            self.saveImage.setDisabled(False)
            self.procImage(self.filename)

    def savePdf(self, file):
        colors = self.colors
        imgfile = self.filename
        canvas = Canvas(file, pagesize=A4)
        pdfmetrics.registerFont(TTFont('Arial', 'font/Arial.ttf'))
        canvas.setFont('Arial', 16)
        canvas.drawString(20, 800, u"Доминирующие цвета")
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
