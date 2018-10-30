from PyQt4 import QtCore, QtGui
import sys
import MainMenu
from tkinter import *

list1 = []
list2 = []

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_mainMenu(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, mainMenu):
        mainMenu.setObjectName(_fromUtf8("mainMenu"))
        mainMenu.resize(404, 334)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainMenu.sizePolicy().hasHeightForWidth())
        mainMenu.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(mainMenu)
        self.label.setGeometry(QtCore.QRect(10, 10, 99, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(mainMenu)
        self.label_2.setGeometry(QtCore.QRect(230, 310, 171, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.search_btn = QtGui.QPushButton(mainMenu)
        self.search_btn.setGeometry(QtCore.QRect(210, 70, 181, 41))
        self.search_btn.setAutoDefault(True)
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.scrollArea = QtGui.QScrollArea(mainMenu)
        self.scrollArea.setGeometry(QtCore.QRect(9, 119, 381, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.console_out = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.console_out.setGeometry(QtCore.QRect(0, 0, 381, 141))
        self.console_out.setObjectName(_fromUtf8("console_out"))
        item = QtGui.QListWidgetItem()
        self.console_out.addItem(item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.copyCity_btn = QtGui.QPushButton(mainMenu)
        self.copyCity_btn.setGeometry(QtCore.QRect(270, 270, 121, 31))
        self.copyCity_btn.setObjectName(_fromUtf8("copyCity_btn"))
        self.line = QtGui.QFrame(mainMenu)
        self.line.setGeometry(QtCore.QRect(7, 300, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.copyState_btn = QtGui.QPushButton(mainMenu)
        self.copyState_btn.setGeometry(QtCore.QRect(140, 270, 121, 31))
        self.copyState_btn.setObjectName(_fromUtf8("copyState_btn"))
        self.clearList_btn = QtGui.QPushButton(mainMenu)
        self.clearList_btn.setGeometry(QtCore.QRect(10, 270, 121, 31))
        self.clearList_btn.setObjectName(_fromUtf8("clearList_btn"))
        self.lineEdit = QtGui.QLineEdit(mainMenu)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century"))
        font.setPointSize(18)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        mainMenu.setWindowTitle(_translate("mainMenu", "QA Tools - ZipCity", None))
        self.label.setText(_translate("mainMenu", "ZipCity", None))
        self.label_2.setText(_translate("mainMenu", "Innovative Enterprises Inc. - 2016", None))
        self.search_btn.setText(_translate("mainMenu", "Search", None))
        __sortingEnabled = self.console_out.isSortingEnabled()
        self.console_out.setSortingEnabled(False)
        self.console_out.setSortingEnabled(__sortingEnabled)
        self.copyCity_btn.setText(_translate("mainMenu", "Copy QA Code (City)", None))
        self.copyState_btn.setText(_translate("mainMenu", "Copy QA Code (State)", None))
        self.clearList_btn.setText(_translate("mainMenu", "Clear List", None))
        self.search_btn.clicked.connect(self.runZipCity)
        self.clearList_btn.clicked.connect(self.clearAll)
        self.copyCity_btn.clicked.connect(self.copyCity)
        self.copyState_btn.clicked.connect(self.copyState)
        self.lineEdit.returnPressed.connect(self.search_btn.click)
        self.lineEdit.returnPressed.connect(self.clearSearch)

    def clearSearch(self):
        self.lineEdit.setText(_translate("mainMenu", "", None))

    def clearAll(self):
        global list1
        global list2
        list1 = []
        list2 = []
        self.console_out.clear()
        self.lineEdit.setText(_translate("mainMenu", "", None))

    def copyCity(self):
        x = Tk()
        x.withdraw()
        x.clipboard_clear()
        for i in list1:
            x.clipboard_append(i + '\n')

    def copyState(self):
        x = Tk()
        x.withdraw()
        x.clipboard_clear()
        for i in list2:
            x.clipboard_append(i + '\n')

    def runZipCity(self):
        import zips

        def zip_state_lookup(x):
            global list1
            citystate = zips.zips[x[:5]].split(',')
            city = citystate[0]
            state = citystate[1]
            self.console_out.addItem('The zip code %s is in the city %s and state %s' % (x, city, state))
            sql = "\tWhen Zip = '%s' then '%s'" % (x, city)
            list1.append(sql)
            sqlst = "\tWhen Zip = '%s' then '%s'" % (x, state)
            list2.append(sqlst)

        def start():
            global list1
            global list2
            entry = str(self.lineEdit.text())

            if "\n" in entry:
                listOfEntries = entry.split("\n")
                for entries in listOfEntries:
                    if entries.strip().replace("-", "").isdigit() == True and zips.zips.get(entries.strip()[:5]) != None:
                        zip_state_lookup(entries.strip())
                    elif entries.strip().isdigit() == True and zips.zips.get(entries.strip()) == None:
                        self.console_out.addItem('The zip code %s does not exist' % entries.strip())
            else:
                if entry.replace("-", "").isdigit() == True and zips.zips.get(entry[:5]) != None:
                    zip_state_lookup(entry)
                elif entry.isdigit() == True and zips.zips.get(entry) == None:
                    self.console_out.addItem('The zip code %s does not exist' % entry)

        start()


def runZipCityFromMenu():
    ex = Ui_mainMenu()
    ex.show()
    MainMenu.app.exec_()
