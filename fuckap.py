#by kotivas
#PyQt6

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from sys import argv
import time

class Ui(QtWidgets.QMainWindow): # класс ебать основного окна
    def __init__(self): # Инициализация окна
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.stupid = self.findChild(QtWidgets.QPushButton, 'pushButton') # ванез тупой ебать
        self.stupid.clicked.connect(self.ImStupid)

        self.showHistory = self.findChild(QtWidgets.QPushButton, 'pushButton_2') # кнопка показать историю ебать
        self.showHistory.clicked.connect(self.openHistory)

        self.all = self.findChild(QtWidgets.QLabel, 'label') # строка отображения всего факапов ебать

        self.today = self.findChild(QtWidgets.QLabel, 'label_2') # строчка отображения факапов сегодня ебать
        
        self.UpdateFuckaps(write=False)

        self.show() 
    
    def closeEvent(self, event):
        self.UpdateFuckaps(write=True)
        print("writed")

    def openHistory(self):
        self.hstry = History()
        self.hstry.show()

    def UpdateFuckaps(self, write):
        global counter

        f = open("all.txt", "r+") # открытие файла
        readed = f.readlines()

        total = len(readed) + counter #факапов всего
        currentTime = str(QDate.currentDate().day()) + "." + str(QDate.currentDate().month())# текущее время

        if write:
            f.write("{0} - {1} раз(-а)\n".format(currentTime, counter))

        self.all.setText("всего: {0}".format(total))

        f.close()

    def ImStupid(self):
        global counter
        counter += 1

class History(QtWidgets.QWidget): # класс окна истории ебать
    def __init__(self):
        super(History, self).__init__()
        uic.loadUi('history.ui', self)
        
        self.historyList = self.findChild(QtWidgets.QListWidget, 'listWidget') # отображение истории факапов ебать
        self.historyList.itemClicked.connect(self.openEdit)

        self.show()

    def openEdit(self):
        self.d = Edit()
        self.d.show()

class Edit(QtWidgets.QWidget):
    def __init__(self):
        super(Edit, self).__init__()
        uic.loadUi('edit.ui', self)

        self.ImTooLazyToMakeaName = self.findChild(QtWidgets.QListWidget, 'listWidget') # отображение факапов за день ебать

        self.day = self.findChild(QtWidgets.QListWidget, 'listWidget') # отображение дня ебать

if __name__ == "__main__": # ну эт крч что бы работало

    counter = 0


    app = QtWidgets.QApplication(argv)
    window = Ui()

    app.exec() # запуск основного окна



