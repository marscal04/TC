# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow02.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setEnabled(True)
        LoginWindow.resize(482, 447)
        LoginWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        LoginWindow.setWindowTitle("")
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QFrame(self.centralwidget)
        self.login.setStyleSheet("background-color: rgb(0,0,0);")
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_2 = QtWidgets.QFrame(self.login)
        self.login_2.setMaximumSize(QtCore.QSize(250, 300))
        self.login_2.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 4px;")
        self.login_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_2.setObjectName("login_2")
        self.emailEdit = QtWidgets.QLineEdit(self.login_2)
        self.emailEdit.setGeometry(QtCore.QRect(40, 135, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailEdit.setFont(font)
        self.emailEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(126, 126, 126)\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(20, 20, 20);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgb(255, 245, 140);\n"
"    color: rgb(244, 244, 244);\n"
"}")
        self.emailEdit.setObjectName("emailEdit")
        self.okButton = QtWidgets.QPushButton(self.login_2)
        self.okButton.setGeometry(QtCore.QRect(60, 180, 120, 20))
        self.okButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(57, 57, 57);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(90, 90, 90);\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.okButton.setObjectName("okButton")
        self.loginLabel = QtWidgets.QLabel(self.login_2)
        self.loginLabel.setGeometry(QtCore.QRect(60, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(28)
        font.setItalic(True)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: rgb(85, 255, 255);")
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout_2.addWidget(self.login_2)
        self.horizontalLayout.addWidget(self.login)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        self.emailEdit.setPlaceholderText(_translate("LoginWindow", "  Email"))
        self.okButton.setText(_translate("LoginWindow", "OK"))
        self.loginLabel.setText(_translate("LoginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
