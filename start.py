#!/usr/bin/env python3

import sys
from time import time
from core import design
from core.image_collector import ImageCollector
from core.pdf_generator import PdfGenerator, CAN_GENERATE_PDF
from PyQt6 import QtWidgets, QtGui, QtCore

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
        self._colors = self.colors_thread.colors

        rtoh = lambda rgb: '%s' % ''.join(('%02x' % p for p in rgb))
        self.colors = list(map(rtoh, self._colors))

        self._pix_original = QtGui.QPixmap()
        self._pix_original.load(self.filename)

        self._scaleImage()

        self.colorsLayout(self.colors)

        self.statusBar().showMessage("Выполнено за {} сек.".format(round(time() - self.start, 3)))
        self.refreshImageAction.setDisabled(False)

    def _scaleImage(self):
        if not hasattr(self, '_pix_original') or self._pix_original.isNull():
            return

        available_w = self.imgLabel.width()
        available_h = self.imgLabel.height()

        if available_w <= 0 or available_h <= 0:
            return

        pix = self._pix_original.scaled(
            available_w, available_h,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation
        )
        self.imgLabel.setPixmap(pix)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._scaleImage()

    def procImage(self, filename: str):
        self.refreshImageAction.setDisabled(True)
        self.start = time()
        self.filename = filename

        self.colors_thread = ImageCollector(filename, self.spinBox.value())
        self.colors_thread.finished.connect(self._procImageDone)
        self.colors_thread.start()

    def showDialog(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(
            caption="Открыть изображение",
            filter="Изображения (*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tiff)"
        )[0]
        if self.filename:
            self.refreshImageAction.setDisabled(False)
            self.saveImage.setDisabled(False)
            self.procImage(self.filename)

    def saveDialog(self):
        if not CAN_GENERATE_PDF:
            return self.message('Не установлена библиотека reportlab')

        file = QtWidgets.QFileDialog.getSaveFileName(caption="Сохранить изображение", filter="PDF (*.pdf)")[0]

        if not file:
            return

        if not file.lower().endswith('.pdf'):
            file += '.pdf'

        self.savePdf(file)

    def savePdf(self, file: str):
        colors = self.colors
        imgfile = self.filename
        
        generator = PdfGenerator()
        success = generator.save_pdf(file, colors, imgfile)
        
        if not success:
            return self.message('Ошибка при сохранении PDF')

    def refreshImage(self):
        self.procImage(self.filename)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
