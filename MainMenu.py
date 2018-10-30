from PyQt4 import QtCore, QtGui
import sys
import RunQAGUI
import RunZipCityGUI
import threading
import os

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
        self.runZipCity_btn = QtGui.QPushButton(mainMenu)
        self.runZipCity_btn.setGeometry(QtCore.QRect(220, 130, 151, 71))
        self.runZipCity_btn.setObjectName(_fromUtf8("runZipCity_btn"))
        self.runQA_btn = QtGui.QPushButton(mainMenu)
        self.runQA_btn.setGeometry(QtCore.QRect(30, 130, 151, 71))
        self.runQA_btn.setObjectName(_fromUtf8("runQA_btn"))
        self.label_2 = QtGui.QLabel(mainMenu)
        self.label_2.setGeometry(QtCore.QRect(230, 310, 171, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        mainMenu.setWindowTitle(_translate("mainMenu", "QA Tools", None))
        self.label.setText(_translate("mainMenu", "QA Tools", None))
        self.runZipCity_btn.setText(_translate("mainMenu", "Run Zip City", None))
        self.runQA_btn.setText(_translate("mainMenu", "Run QA", None))
        self.label_2.setText(_translate("mainMenu", "Innovative Enterprises Inc. - 2016", None))
        self.runQA_btn.clicked.connect(self.runQAAppFromButton)
        self.runZipCity_btn.clicked.connect(self.runZipCityFromButton)

    def runQAAppFromButton(self):
        RunQAGUI.runQAFromMenu()

    def runZipCityFromButton(self):
        RunZipCityGUI.runZipCityFromMenu()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_mainMenu()
    ex.show()
    os._exit(app.exec_())
