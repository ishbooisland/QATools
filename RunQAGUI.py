import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PyQt4 import QtCore, QtGui
import sys
import pyodbc
import os
import threading
import MainMenu
import time
import re

Today = time.strftime("%Y%m%d")

sourceList = []
server = ""
fileNumber = 1


def getSources():
    global sourceList
    sourceList = getSQLList(
        "Select Distinct Replace(Replace(Name,'_OnlineIndex',''),'_Offenses','') From Sys.Tables Order by Replace(Replace(Name,'_OnlineIndex',''),'_Offenses','')")


def getSQLList(query):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DARRIN-PC\SQLEXPRESS;DATABASE=Test')
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


getSources()

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
        self.sunken_frame = QtGui.QFrame(mainMenu)
        self.sunken_frame.setGeometry(QtCore.QRect(10, 80, 241, 31))
        self.sunken_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sunken_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.sunken_frame.setObjectName(_fromUtf8("sunken_frame"))
        self.dir_lbl = QtGui.QLabel(self.sunken_frame)
        self.dir_lbl.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.dir_lbl.setMinimumSize(QtCore.QSize(0, 13))
        self.dir_lbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dir_lbl.setObjectName(_fromUtf8("dir_lbl"))
        self.browse_btn = QtGui.QPushButton(mainMenu)
        self.browse_btn.setGeometry(QtCore.QRect(270, 80, 121, 31))
        self.browse_btn.setObjectName(_fromUtf8("browse_btn"))
        self.scrollArea = QtGui.QScrollArea(mainMenu)
        self.scrollArea.setGeometry(QtCore.QRect(9, 119, 381, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.source_list = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.source_list.setGeometry(QtCore.QRect(0, 0, 381, 141))
        self.source_list.setObjectName(_fromUtf8("source_list"))
        for source in sourceList:
            self.source_list.addItem(str(source[0]))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.runQA_btn = QtGui.QPushButton(mainMenu)
        self.runQA_btn.setGeometry(QtCore.QRect(270, 270, 121, 31))
        self.runQA_btn.setObjectName(_fromUtf8("runQA_btn"))
        self.progressBar = QtGui.QProgressBar(mainMenu)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 241, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.line = QtGui.QFrame(mainMenu)
        self.line.setGeometry(QtCore.QRect(7, 300, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        mainMenu.setWindowTitle(_translate("mainMenu", "QA Tools - Run QA", None))
        self.label.setText(_translate("mainMenu", "Run QA", None))
        self.label_2.setText(_translate("mainMenu", "Innovative Enterprises Inc. - 2016", None))
        self.dir_lbl.setText(_translate("mainMenu", "Choose QA Results Folder...", None))
        self.browse_btn.setText(_translate("mainMenu", "Browse", None))
        self.runQA_btn.setText(_translate("mainMenu", "Run QA", None))
        self.browse_btn.clicked.connect(self.setExistingDirectory)
        self.runQA_btn.clicked.connect(self.launch_RunQA_Thread)

    def setExistingDirectory(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Choose QA Results Folder",
                                                           self.dir_lbl.text(), options)
        if directory:
            self.dir_lbl.setText(directory)
            self.QtGui.QFileDialog.setDirectory(directory)

    def launch_RunQA_Thread(self):
        t = threading.Thread(target=self.RunQAResults)
        t.start()

    def updateProgress(self, percentage):
        self.progressBar.setProperty("value", percentage)
        self.progressBar.update()

    def reportError(self, errorMessage):
        self.errorDialog = QtGui.QMessageBox()
        self.errorDialog.setText(errorMessage)
        self.errorDialog.exec_()

    def RunQAResults(self):

        qaDirectory = self.dir_lbl.text()
        inputSource = self.source_list.currentItem().text()

        if '\\QA Results' not in qaDirectory:
            qaDirectory += '\\QA Results\\'
        elif qaDirectory[:1] != "\\":
            qaDirectory += "\\"

        def cleanSpaces(input):
            return input.replace('\r', ' ').replace('\n', ' ').replace(' ', '{}').replace('}{', '').replace('{}', ' ')

        def appendLine(filename, text):
            with open(filename, 'a') as g:
                g.write(text)

        def runOnlineIndex(sourceInput, directory):
            global fileNumber

            try:
                queriesOI = getSQLList(
                    "Select F1 From Zeus.Data_Dev.dbo.Online_Index_Prints " +
                    "Order by ID")
                source = sourceInput

                if not os.path.isdir(directory):
                    os.mkdir(directory)

                from os import listdir
                from os.path import isfile, join
                files = [f for f in listdir(str(directory)) if isfile(join(str(directory), f))]

                while 1:
                    if any("_QA" + str(fileNumber) in s for s in files):
                        fileNumber += 1
                    else:
                        break

                with open(directory + source + '_Online_Index_' + Today + '_QA' + str(fileNumber) + '.sql', 'w') as f:
                    f.write(source)

                currentQuery = 0
                totalQueryCount = len(queriesOI)

                for query in queriesOI:
                    currentQuery += 1

                    if currentQuery % 2 == 0:
                        percentageComplete = float(currentQuery / float(totalQueryCount) * 100)
                        self.updateProgress(percentageComplete)

                    results = getSQLList(query.F1.replace('xxxxx', source))

                    if len(results) > 0:
                        appendLine(directory + source + '_Online_Index_' + Today + '_QA' + str(fileNumber) + '.sql',
                                   '\n\n' + query.F1.replace('xxxxx', source))
                        for result in results:
                            amountOfColumns = len(result)
                            resultToPrint = ''

                            for i in range(0, amountOfColumns):
                                if result[i] is None:
                                    resultToPrint = resultToPrint + '' + '|'
                                else:
                                    resultToPrint = resultToPrint + str(result[i]).decode("latin1").encode('utf-8') + '|'

                            appendLine(directory + source + '_Online_Index_' + Today + '_QA' + str(fileNumber) + '.sql',
                                       '\n' + str(resultToPrint).decode("latin1").encode('utf-8'))

                        appendLine(directory + source + '_Online_Index_' + Today + '_QA' + str(fileNumber) + '.sql',
                                   '\n\n' +
                                   'Rows Affected(' + str(len(results)) + ')')
                        appendLine(directory + source + '_Online_Index_' + Today + '_QA' + str(fileNumber) + '.sql',
                                   '\n' +
                                   '-----------------------------------------------------------------------------------' +
                                   '------------------------------------------------------------------------------------')
                    results = ''
            except Exception as e:
                self.reportError('An Error Has Occurred: ' + str(e))
                raise threading.ThreadError("Error")

        def runOffenses(sourceInput, directory):
            global fileNumber

            try:
                queriesOF = getSQLList("Select F1 From Zeus.Data_Dev.dbo.Offenses_Prints Order by ID")
                source = sourceInput

                if not os.path.isdir(directory):
                    os.mkdir(directory)

                with open(directory + source + '_Offenses_' + Today + '_QA' + str(fileNumber) + '.sql', 'w') as f:
                    f.write(source)

                currentQuery = 0
                totalQueryCount = len(queriesOF)

                for query in queriesOF:
                    currentQuery += 1

                    if currentQuery % 2 == 0:
                        percentageComplete = float(currentQuery / float(totalQueryCount) * 100)
                        self.updateProgress(percentageComplete)

                    results = getSQLList(query.F1.replace('xxxxx', source))

                    if len(results) > 0:
                        appendLine(directory + source + '_Offenses_' + Today + '_QA' + str(fileNumber) + '.sql',
                                   '\n\n' + query.F1.replace('xxxxx', source))
                        for result in results:
                            amountOfColumns = len(result)
                            resultToPrint = ''

                            for i in range(0, amountOfColumns):
                                if result[i] is None:
                                    resultToPrint = resultToPrint + '' + '|'
                                else:
                                    resultToPrint = resultToPrint + str(result[i]).decode("latin1").encode('utf-8') + '|'

                            appendLine(directory + source + '_Offenses_' + Today + '_QA' + str(fileNumber) + '.sql',
                                       '\n' + str(resultToPrint).decode("latin1").encode('utf-8'))

                        appendLine(directory + source + '_Offenses_' + Today + '_QA' + str(fileNumber) + '.sql',
                                   '\n\n' +
                                   'Rows Affected(' + str(len(results)) + ')')
                        appendLine(directory + source + '_Offenses_' + Today + '_QA' + str(fileNumber) + '.sql', '\n' +
                                   '-----------------------------------------------------------------------------------' +
                                   '------------------------------------------------------------------------------------')
                    results = ''
            except Exception as e:
                self.reportError('An Error Has Occurred: ' + str(e))
                raise threading.ThreadError("Error")

        runOnlineIndex(inputSource, qaDirectory)
        runOffenses(inputSource, qaDirectory)
        self.reportError('QA Prints Are Complete')


def runQAFromMenu():
    ex = Ui_mainMenu()
    ex.show()
    MainMenu.app.exec_()
