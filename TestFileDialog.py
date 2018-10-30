import sip

sip.setapi('QString', 2)

import sys
from PyQt4 import QtCore, QtGui


class Dialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QtGui.QErrorMessage(self)

        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.Panel

        self.directoryLabel = QtGui.QLabel()
        self.directoryLabel.setFrameStyle(frameStyle)
        self.directoryButton = QtGui.QPushButton("Browse")

        self.directoryButton.clicked.connect(self.setExistingDirectory)

        layout = QtGui.QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.directoryButton, 6, 0)
        layout.addWidget(self.directoryLabel, 6, 1)
        self.setLayout(layout)

        self.setWindowTitle("Standard Dialogs")

    def setExistingDirectory(self):
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Choose QA Results Folder",
                                                           self.directoryLabel.text(), options)
        if directory:
            self.directoryLabel.setText(directory)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
