#code by kotivas
#idea by VaneZ#2039 (DISCORD)
#PyQt6

#----todo-list----
# пофиксить баг, когда старое описание факапа стирается [СДЕЛАНО]
# пофиксить баг, когда надо перезапустить прогу, что бы обновилась история факапов
# пофиксить баг, когда прога не работает если файл ./all.txt пустой, прога не работает [СДЕЛАНО]
# добавить функцию изменения описания факапа через gui

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
            readed = f.readlines() # чтение файла

        except FileNotFoundError:
            f = open("all.txt", "w") # создание файла
            readed = []
        f.close()

        if readed == []: # если файл пуст
            readed = ["0.0;0;0 - NO:\n"] # он заполняется пустышкой

        for i in range(0, len(readed)): # счёт всех факапов
            tmp = readed[i].split(";")
            total += int(tmp[1])

        desc = tmp[2][:-1]
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

                if len(desc.split(":"))-1 != todayCounter: # если количество описаний факапов, не соотвествует кол-ву факапов
                    startFrom = len(desc.split(":"))-1
                    for i in range(startFrom, todayCounter):
                        desc += "{0} - no:".format(i+1) # в конец добавляются недостающие факапы

                counter += int(tmp[1])
            
            else:
                for i in range(0, len(readed)):
                    f.write(readed[i])
                
                desc = ""
                for i in range(1, counter+1):
                    desc += "{0} - no:".format(i)

            f.write("{0};{1};{2}\n".format(currentTime, counter, desc))

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

        self.getFuckup() # получение факапов

    def openfEdit(self): # открытие изменение описания факапа
        global dateANDcount

        item = self.ImTooLazyToMakeaName.currentItem().text()

        dateANDcount = date + " - " + item[:-4]

        self.d = fEdit()
        self.d.show()

    def getFuckup(self):
        global date

        f = open("all.txt", "r")
        readed = f.readlines()
        
        self.day.setText("{0}:".format(date)) # установка даты

        for i in range(1, len(readed)): # добавление всех факапов текущего дня
            tmp = readed[i].split(";")
            if tmp[0] == date:
                for i in range(0, int(tmp[1])):
                    self.ImTooLazyToMakeaName.addItem(tmp[2].split(":")[i])

class fEdit(QtWidgets.QWidget):
    def __init__(self):
        super(fEdit, self).__init__()
        uic.loadUi('fEdit.ui', self)
        global dateANDcount

        self.data = self.findChild(QtWidgets.QLabel, 'label')
        self.data.setText(dateANDcount)

        self.editline = self.findChild(QtWidgets.QTextEdit, 'textEdit')

    def closeEvent(self, event):
        global output
        output = self.editline.toPlainText()

if __name__ == "__main__": # ну эт крч что бы работало

    counter = 0

    app = QtWidgets.QApplication(argv)
    window = Ui()

    app.exec() # запуск основного окна



