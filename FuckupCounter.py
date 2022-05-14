#code by kotivas
#idea by VaneZ#2039 
#PyQt6

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from sys import argv

class Ui(QtWidgets.QMainWindow): # класс ебать основного окна
    def __init__(self): # Инициализация окна
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.stupid = self.findChild(QtWidgets.QPushButton, 'pushButton') # ванез лох ебать
        self.stupid.clicked.connect(self.ImStupid)

        self.showHistory = self.findChild(QtWidgets.QPushButton, 'pushButton_2') # кнопка показать историю ебать
        self.showHistory.clicked.connect(self.openHistory)

        self.all = self.findChild(QtWidgets.QLabel, 'label') # строка отображения всего факапов ебать

        self.today = self.findChild(QtWidgets.QLabel, 'label_2') # строчка отображения факапов сегодня ебать
        
        self.UpdateFuckaps(write=False)

        self.show() 
    
    def closeEvent(self, event):
        self.UpdateFuckaps(write=True)

    def openHistory(self):

        self.hstry = History()
        self.hstry.show()

    def UpdateFuckaps(self, write):
        global counter, readed
        
        total  = 0
        todayCounter = 0

        try:
            f = open("all.txt", "r+") # открытие файла
        except FileNotFoundError:
            f = open("all.txt", "w+")
            f.write("1.1;0;\n")
            tmp = ["1.1", "0"]

        readed = f.readlines()
        f.close()
        
        for i in range(0, len(readed)): # счёт всех факапов
            tmp = readed[i].split(";")
            total += int(tmp[1])

        total += counter 
        currentTime = str(QDate.currentDate().day()) + "." + str(QDate.currentDate().month())# текущее время

        if tmp[0] == currentTime:
            todayCounter += int(tmp[1])

        todayCounter += counter

        if write: # запсиь факапов в файл
            f = open("all.txt", "w") # открытие файла на запись
                
            if tmp[0] == currentTime: # если последняя строчка имеет дату которая равна текущей 
                for i in range(0, len(readed[:-1])): # запись всех факапов, кроме последнего
                    f.write(readed[i])
                counter += int(tmp[1])
 
            else:
                for i in range(0, len(readed)):
                    f.write(readed[i])


            f.write("{0};{1};\n".format(currentTime, counter))

            f.close()

        self.all.setText("всего: {0}".format(total))
        self.today.setText("за сегодня: {0}".format(todayCounter))

    def ImStupid(self):
        global counter
        counter += 1

        self.UpdateFuckaps(write=False)

class History(QtWidgets.QWidget): # класс окна истории ебать
    def __init__(self):
        super(History, self).__init__()
        uic.loadUi('history.ui', self)
        
        self.historyList = self.findChild(QtWidgets.QListWidget, 'listWidget') # отображение истории факапов ебать
        self.historyList.itemClicked.connect(self.openEdit)

        self.getHistory() # получение и запись истории факапов 

    def openEdit(self):
        global date
        
        item = self.historyList.currentItem().text()

        date = item[0] + item[1] + item[2] + item[3]

        print(date)

        self.d = Edit()
        self.d.show()

    def getHistory(self):
        f = open("all.txt", "r")
        readed = f.readlines()

        for i in range(1, len(readed)):
            tmp = readed[i].split(";")

            self.historyList.addItem("{0} - {1} раз(а)".format(tmp[0], tmp[1]))
        f.close()


class Edit(QtWidgets.QWidget):
    def __init__(self):
        super(Edit, self).__init__()
        uic.loadUi('edit.ui', self)

        self.ImTooLazyToMakeaName = self.findChild(QtWidgets.QListWidget, 'listWidget') # отображение факапов за день ебать
        self.ImTooLazyToMakeaName.itemClicked.connect(self.openfEdit)

        self.day = self.findChild(QtWidgets.QLabel, 'label') # отображение дня ебать

        self.getFuckup()

    def openfEdit(self):

        self.d = fEdit()
        self.d.show()

    def getFuckup(self):
        global date

        f = open("all.txt", "r")
        readed = f.readlines()
        
        self.day.setText("{0}:".format(date))

        for i in range(1, len(readed)):
            tmp = readed[i].split(";")
            if tmp[0] == date:
                for i in range(0, int(tmp[1])):
                    #print(tmp[1])
                    self.ImTooLazyToMakeaName.addItem("{0} - нет".format(i+1))

class fEdit(QtWidgets.QWidget):
    def __init__(self):
        super(fEdit, self).__init__()
        uic.loadUi('fEdit.ui', self)

        self.data = self.findChild(QtWidgets.QLabel, 'label')

        self.editline = self.findChild(QtWidgets.QTextEdit, 'textEdit')

if __name__ == "__main__": # ну эт крч что бы работало

    counter =0

    app = QtWidgets.QApplication(argv)
    window = Ui()

    app.exec() # запуск основного окна



