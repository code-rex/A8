# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(830, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"background-color: #ffffff;\n"
"}"))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 250, 291, 51))
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
        self.lineEdit.setGeometry(QtCore.QRect(420, 140, 291, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 200, 291, 31))
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
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("QLabel\n"
"{color : #00b3b3    }"))
        self.label_3.setTextFormat(QtCore.Qt.LogText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 330, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(114)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QLabel\n"
"{color : #00b3b3    }"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 360, 141, 16))
        self.label_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_2.setStyleSheet(_fromUtf8("QLabel\n"
"{color : #00b300    }\n"
"QLabel\n"
"{color : #00b3b3    }"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 46, 13))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 90, 301, 311))
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/pid.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "USERNAME", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "PASSWORD", None))
        self.label_3.setText(_translate("MainWindow", "LOGIN", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Create a New Account</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Forgot Password ?</span></p></body></html>", None))

import new_rc
if __name__=="__main__":
    import sys
    app=QtGui.QApplication(sys.argv)
    MainWindow=QtGui.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
