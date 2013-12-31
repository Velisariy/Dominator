import sys
from time import time
from core import core
from PyQt4 import QtCore, QtGui


class MainWindow(QtGui.QMainWindow):
    '''
    Визуальная оболочка для вычисления доминирующих цветов в изображении
    '''
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(640, 480)
        self.setWindowTitle("Доминатор")
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.statusBar()

        self.openImage = QtGui.QAction(QtGui.QIcon('icons/fileopen.png'), 'Открыть файл', self)
        self.openImage.setShortcut('Ctrl+O')
        self.connect(self.openImage, QtCore.SIGNAL("triggered()"), self.showDialog)

        self.refreshImageAction = QtGui.QAction(QtGui.QIcon('icons/refresh.png'), 'Обновить', self)
        # Выключаем кнопку Обновить при запуске программы
        self.refreshImageAction.setDisabled(True)  
        self.connect(self.refreshImageAction, QtCore.SIGNAL('triggered()'), self.refreshImage)

        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Выход', self)
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # Отвечает за счетчик количества цветов. По умолчанию 3.
        self.spinBox = QtGui.QSpinBox()
        self.spinBox.setRange(1, 6)
        self.spinBox.setValue(3)

        toolBar = self.addToolBar('Панель инструментов')
        toolBar.addAction(self.openImage)
        toolBar.addSeparator()
        toolBar.addWidget(self.spinBox)
        toolBar.addAction(self.refreshImageAction)
        toolBar.addSeparator()
        toolBar.addAction(self.exit)

        self.imgLabel = QtGui.QLabel()
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        # Текст приветствия в окне
        helloText = QtGui.QTextBrowser()
        f = open("hello.html", mode="r", encoding="cp1251")
        helloText.setHtml(f.read())
        f.close()
        self.setCentralWidget(helloText)

    def procImage(self, filename):
        start = time()
        # Определяем список доминирующих цветов
        colors = list(core.colorz(filename, self.spinBox.value()))
        colors.sort()
        # Загружаем изображение и редактируем его
        pix = QtGui.QPixmap()
        pix.load(filename)
        w = pix.width() * 1.0
        h = pix.height() * 1.0
        k = round(w / h, 2)

        self.imgLabel.setPixmap(pix.scaled(600 * k, 600))

        def matching(color):
            '''
            Сравнение цвета со средним значением
            для читабельного отображения текста
            '''
            if int(color, 16) > int("888888", 16):
                result = "black"
            else:
                result = "white"
            return result
            
        self.hBoxColor = QtGui.QHBoxLayout()
        self.hBoxColor.setMargin(0)
        colorWidgets = []
        labelWidgets = []
        vBoxLabels = []
        for key, color in enumerate(colors):
            colorWidgets.append(QtGui.QWidget())
            labelWidgets.append(QtGui.QLabel())
            vBoxLabels.append(QtGui.QVBoxLayout())
            vBoxLabels[key].setMargin(0)

            self.hBoxColor.addWidget(colorWidgets[key])

            # Отображаем один из доминирующих цветов
            colorWidgets[key].setStyleSheet("QWidget { background-color: #%s }" % color)
            colorWidgets[key].setLayout(vBoxLabels[key])

            vBoxLabels[key].addWidget(labelWidgets[key])

            labelWidgets[key].setText("#%s" % color)
            labelWidgets[key].setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            labelWidgets[key].setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
            labelWidgets[key].setStyleSheet("QWidget { color: %s }" % matching(color))
        # Добавляем полученный набор виджетов на экран
        paint = QtGui.QWidget()
        paint.setMaximumHeight(40)
        paint.setMinimumHeight(40)
        paint.setLayout(self.hBoxColor)

        vBox = QtGui.QVBoxLayout()
        vBox.addWidget(paint)
        vBox.addWidget(self.imgLabel)

        mainWidget = QtGui.QWidget()
        mainWidget.setLayout(vBox)

        self.setCentralWidget(mainWidget)
        self.statusBar().showMessage("Выполнено за {} сек.".format(round(time() - start, 3)))

    def showDialog(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, caption="Открыть изображение")
        if self.filename:
            self.refreshImageAction.setDisabled(False)
            self.procImage(self.filename)

    def refreshImage(self):
        self.procImage(self.filename)

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
