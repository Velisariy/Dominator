# coding: UTF-8

import sys
from time import time
from core import core
from PyQt5 import QtWidgets, QtCore, QtGui

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor


class MainWindow(QtWidgets.QMainWindow):
    """
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.resize(640, 480)
        self.colors = []
        self.filename = ''
        self.setWindowTitle(u"Доминатор")
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))

        self.openImage = QtWidgets.QAction(QtGui.QIcon('icons/fileopen.png'), u'Открыть файл', self)
        self.openImage.setShortcut('Ctrl+O')
        self.openImage.triggered.connect(self.showDialog)

        self.saveImage = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Сохранить', self)
        self.saveImage.setShortcut('Ctrl+S')
        self.saveImage.setDisabled(True)
        self.saveImage.triggered.connect(self.saveDialog)

        self.refreshImageAction = QtWidgets.QAction(QtGui.QIcon('icons/refresh.png'), u'Обновить', self)
        self.refreshImageAction.setDisabled(True)
        self.refreshImageAction.triggered.connect(self.refreshImage)

        self.exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), u'Выход', self)
        self.exit.triggered.connect(self.close)

        # Отвечает за счетчик количества цветов. По умолчанию 3.
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setRange(1, 15)
        self.spinBox.setValue(3)

        toolBar = self.addToolBar(u'Панель инструментов')
        toolBar.addAction(self.openImage)
        toolBar.addAction(self.saveImage)
        toolBar.addSeparator()
        toolBar.addWidget(self.spinBox)
        toolBar.addAction(self.refreshImageAction)
        toolBar.addSeparator()
        toolBar.addAction(self.exit)

        self.imgLabel = QtWidgets.QLabel()
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        # Текст приветствия в окне
        helloText = QtWidgets.QTextBrowser()
        f = open("hello.html", mode="r", encoding="utf8")
        helloText.setHtml(f.read())
        f.close()
        self.setCentralWidget(helloText)

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
        self.hBoxColor = QtWidgets.QHBoxLayout()
        self.hBoxColor.setContentsMargins(0, 0, 0, 0)

        colorWidgets = []
        labelWidgets = []
        vBoxLabels = []
        for key, color in enumerate(self.colors):
            colorWidgets.append(QtWidgets.QWidget())
            labelWidgets.append(QtWidgets.QLabel())
            vBoxLabels.append(QtWidgets.QVBoxLayout())
            vBoxLabels[key].setContentsMargins(0, 0, 0, 0)

            self.hBoxColor.addWidget(colorWidgets[key])

            # Отображаем один из доминирующих цветов
            colorWidgets[key].setStyleSheet("QWidget { background-color: #%s }" % color)
            colorWidgets[key].setLayout(vBoxLabels[key])

            vBoxLabels[key].addWidget(labelWidgets[key])

            labelWidgets[key].setText("#%s" % color)
            labelWidgets[key].setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            labelWidgets[key].setTextInteractionFlags(
                QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
            labelWidgets[key].setStyleSheet("QWidget { color: %s }" % self.matching(color))

        # Добавляем полученный набор виджетов на экран
        paint = QtWidgets.QWidget()
        paint.setMaximumHeight(40)
        paint.setMinimumHeight(40)
        paint.setLayout(self.hBoxColor)

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(paint)
        vBox.addWidget(self.imgLabel)

        mainWidget = QtWidgets.QWidget()
        mainWidget.setLayout(vBox)

        self.setCentralWidget(mainWidget)
        self.statusBar().showMessage(u"Выполнено за {} сек.".format(round(time() - start, 3)))

    def saveDialog(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, caption="Сохранить изображение", filter="*.pdf")[0]
        
        if file:
            self.savePdf(file)

    def showDialog(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, caption=u"Открыть изображение")[0]
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

            canvas.setFillColor(HexColor(self.matching(color)))
            canvas.drawCentredString(50, 775 - 30 * key, '#{}'.format(color))

            canvas.drawImage(imgfile, 100, 390, 300, 400, preserveAspectRatio=True, anchor='nw')

        canvas.save()

    def refreshImage(self):
        self.procImage(self.filename)

    @staticmethod
    def matching(color):
        '''
        Сравнение цвета со средним значением
        для читабельного отображения текста
        '''
        color.strip('#')
        if int(color, 16) > int("888888", 16):
            result = "#000000"
        else:
            result = "#ffffff"
        return result


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
