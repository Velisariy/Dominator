from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QAction, QIcon
from core import core


class MainWindow(QtWidgets.QMainWindow):
    """
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    """

    def __init__(self):
        super().__init__()

        self.resize(640, 480)
        self.setMinimumSize(100, 100)
        self.colors = []
        self.filename = ''
        self.setWindowTitle(u"Доминатор")
        self.setWindowIcon(QIcon('icons/icon.png'))

        self.openImage = QAction(QIcon('icons/fileopen.png'), u'Открыть файл', self)
        self.openImage.setShortcut('Ctrl+O')

        self.saveImage = QAction(QIcon('icons/save.png'), 'Сохранить', self)
        self.saveImage.setShortcut('Ctrl+S')
        self.saveImage.setDisabled(True)

        self.refreshImageAction = QAction(QIcon('icons/refresh.png'), u'Обновить', self)
        self.refreshImageAction.setDisabled(True)

        self.exit = QAction(QIcon('icons/exit.png'), u'Выход', self)
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
        self.imgLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imgLabel.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.imgLabel.setMinimumSize(0, 0)

        # Текст приветствия в окне
        helloText = QtWidgets.QTextBrowser()
        f = open("hello.html", mode="r", encoding="utf8")
        helloText.setHtml(f.read())
        f.close()
        self.setCentralWidget(helloText)

    def message(self, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
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
            labelWidgets[key].setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            labelWidgets[key].setTextInteractionFlags(
                QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
            labelWidgets[key].setStyleSheet("QWidget { color: %s }" % core.matching(color))

        # Добавляем полученный набор виджетов на экран
        paint = QtWidgets.QWidget()
        paint.setFixedHeight(40)
        paint.setLayout(self.hBoxColor)

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(paint, stretch=0)
        vBox.addWidget(self.imgLabel, stretch=1)

        mainWidget = QtWidgets.QWidget()
        mainWidget.setLayout(vBox)
        mainWidget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.setCentralWidget(mainWidget)