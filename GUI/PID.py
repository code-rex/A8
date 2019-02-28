# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PID.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 452)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 190, 211, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 240, 131, 20))
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 140, 151, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 290, 81, 51))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    color: #f6f8ff;\n"
"    border-width: 1px;\n"
"    border-color: #4988af;\n"
"    border-style: solid;\n"
"    border-radius: 15;\n"
"    padding: 5px;\n"
"    font-size: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"  width: 100px;\n"
"  margin-top:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"QPushButton\n"
"{background-color : #00b3b3    }\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 140, 161, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"  color:#323232;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #4988af;\n"
"  border-radius: 10px;\n"
"  padding-left:10px;\n"
"}"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 190, 161, 31))
        self.lineEdit_2.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"  color:#323232;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #4988af;\n"
"  border-radius: 10px;\n"
"  padding-left:10px;\n"
"}"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 240, 161, 31))
        self.lineEdit_3.setStyleSheet(_fromUtf8("QLineEdit\n"
"{\n"
"  color:#323232;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #4988af;\n"
"  border-radius: 10px;\n"
"  padding-left:10px;\n"
"}"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature", None))
        self.label.setText(_translate("MainWindow", "Temperature to be reached :", None))
        self.label_2.setText(_translate("MainWindow", "No.of Intervals :", None))
        self.label_3.setText(_translate("MainWindow", "Initial Temperature :", None))
        self.pushButton.setText(_translate("MainWindow", "START", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "In Centigrade", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "In Centigrade", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Integer", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

