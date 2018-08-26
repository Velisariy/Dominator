# coding: UTF-8

from PyQt5 import QtWidgets, QtCore, QtGui
from core import core


class MainWindow(QtWidgets.QMainWindow):
    """
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    """

    def __init__(self):
        super().__init__()

        self.resize(640, 480)
        self.colors = []
        self.filename = ''
        self.setWindowTitle(u"Доминатор")
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))

        self.openImage = QtWidgets.QAction(QtGui.QIcon('icons/fileopen.png'), u'Открыть файл', self)
        self.openImage.setShortcut('Ctrl+O')

        self.saveImage = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Сохранить', self)
        self.saveImage.setShortcut('Ctrl+S')
        self.saveImage.setDisabled(True)

        self.refreshImageAction = QtWidgets.QAction(QtGui.QIcon('icons/refresh.png'), u'Обновить', self)
        self.refreshImageAction.setDisabled(True)

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

    def message(self, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()

    def colorsLayout(self, colors):

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
            labelWidgets[key].setStyleSheet("QWidget { color: %s }" % core.matching(color))

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