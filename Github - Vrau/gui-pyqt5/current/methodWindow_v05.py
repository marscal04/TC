# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methodWindow_v05.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, QMessageBox
import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências
import re


class Ui_MethodWindow(object):
    def setupUi(self, MethodWindow):
        MethodWindow.setObjectName("MethodWindow")
        MethodWindow.resize(681, 542)
        self.centralwidget = QtWidgets.QWidget(MethodWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(800, 800))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(40,40,40);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color: rgb(85, 82, 125);\n"
"border-radius: 3px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.methodLabel = QtWidgets.QLabel(self.frame_6)
        self.methodLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.methodLabel.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.methodLabel.setFont(font)
        self.methodLabel.setStyleSheet("color:rgb(235, 235, 235)\n"
"")
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodLabel.setObjectName("methodLabel")
        self.horizontalLayout_2.addWidget(self.methodLabel)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tabWidget.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.searchTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.searchTab)
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 3px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(40, 0, 40, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLabel = QtWidgets.QLabel(self.frame_3)
        self.searchLabel.setMaximumSize(QtCore.QSize(350, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.searchLabel.setFont(font)
        self.searchLabel.setStyleSheet("color:rgb(235, 235, 235);\n"
"background-color: rgb(85, 82, 125);\n"
"border-radius: 10px;")
        self.searchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.searchEdit = QtWidgets.QLineEdit(self.frame_4)
        self.searchEdit.setMinimumSize(QtCore.QSize(0, 200))
        self.searchEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.searchEdit.setFont(font)
        self.searchEdit.setStyleSheet("QLineEdit{\n"
"border-radius: 3px;\n"
"}")
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout_4.addWidget(self.searchEdit)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchButton = QtWidgets.QPushButton(self.frame_5)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.searchButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(40,40,40);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(90,90,90);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80,80,80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    border-radius: 3px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_4.addWidget(self.searchButton)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.tabWidget.addTab(self.searchTab, "")
        self.fileTab = QtWidgets.QWidget()
        self.fileTab.setObjectName("fileTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fileTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.fileTab)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setStyleSheet("QFrame{\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 3px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fileEdit = QtWidgets.QLineEdit(self.frame_7)
        self.fileEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fileEdit.setFont(font)
        self.fileEdit.setObjectName("fileEdit")
        self.horizontalLayout_5.addWidget(self.fileEdit)
        self.fileButton = QtWidgets.QPushButton(self.frame_7)
        self.fileButton.setMinimumSize(QtCore.QSize(100, 30))
        self.fileButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(40,40,40);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(90,90,90);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80,80,80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    border-radius: 3px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_5.addWidget(self.fileButton)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.fileTab)
        self.frame_8.setStyleSheet("QFrame{\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 3px;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.seqLabel = QtWidgets.QLabel(self.frame_8)
        self.seqLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seqLabel.setFont(font)
        self.seqLabel.setStyleSheet("color:rgb(235, 235, 235);\n"
"\n"
"")
        self.seqLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.seqLabel.setObjectName("seqLabel")
        self.verticalLayout_6.addWidget(self.seqLabel)
        self.seqEdit = QtWidgets.QLineEdit(self.frame_8)
        self.seqEdit.setMinimumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seqEdit.setFont(font)
        self.seqEdit.setObjectName("seqEdit")
        self.verticalLayout_6.addWidget(self.seqEdit)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setStyleSheet("QFrame{\n"
"    background-color: rgb(76, 76, 76);\n"
"    border-radius: 3px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.insertButton = QtWidgets.QPushButton(self.frame_9)
        self.insertButton.setMinimumSize(QtCore.QSize(0, 30))
        self.insertButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.insertButton.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(40,40,40);\n"
"    color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(90,90,90);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80,80,80);\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 245, 140);\n"
"    border-radius: 3px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"")
        self.insertButton.setObjectName("insertButton")
        self.horizontalLayout_6.addWidget(self.insertButton)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.tabWidget.addTab(self.fileTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MethodWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MethodWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MethodWindow)

        # InMainWindowando o email do usuário
        self.email = Entrez.email = "gabrielgmusskopf@gmail.com"


    def retranslateUi(self, MethodWindow):
        _translate = QtCore.QCoreApplication.translate
        MethodWindow.setWindowTitle(_translate("MethodWindow", "MainWindow"))
        self.methodLabel.setText(_translate("MethodWindow", "Escolha do método"))
        self.searchLabel.setText(_translate("MethodWindow", "Insira o nome ou ID"))
        self.searchButton.setText(_translate("MethodWindow", "Pesquisar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), _translate("MethodWindow", "Pesquisar"))
        self.fileButton.setText(_translate("MethodWindow", "Procurar"))
        self.seqLabel.setText(_translate("MethodWindow", "ou digitar a sequência"))
        self.insertButton.setText(_translate("MethodWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fileTab), _translate("MethodWindow", "Inserir"))

        # Quando botão é clicado, vai para a função fileBrowser()
        self.fileButton.clicked.connect(self.fileBrowser) 
        # Quando botão de pesquisar, verifica se a pesquisa é válida
        self.searchButton.clicked.connect(self.isValidSearch)
        self.insertButton.clicked.connect(self.witchMethod)



    def witchMethod(self):
        # Verifica se foi posto o arquivo ou se foi escrito a sequência
        if self.path != '':
            if re.search("\\b.fasta\\b", self.path, re.IGNORECASE):
                print("A string tem fasta")
                #pesquisa
            else:
                #formato errado -> popup
                pass
        else:
            #pesquisa pela caixa de sequência nucleotídica
            pass

    def localSearch(self):
        pass

    def fileBrowser(self):
        self.openDialogBox()
        # print ("button pressed")

    def openDialogBox(self):
        self.filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
        self.path = self.filename[0]
        self.fileEdit.setText(self.path)
        self.file = open(self.path,"r")
        # print(self.file.read())
        self.popResultLocal(self.file.read())


    def isValidSearch(self):
    # Verifica se o texto é válido

        if self.searchEdit.text() != "":
            print (self.searchEdit.text())
            self.search()
        else:
            print('texto não válido')



    def search(self):
        self.handle = Entrez.esearch(db="nucleotide", term = self.searchEdit.text(), idtype="acc", retmax = 1) 
        self.record = Entrez.read(self.handle) #lendo as infos geradas pela pesquisa
        self.handle.close()

        print (self.handle.url)
        print(self.record["Count"])
        print("ID List: ", self.record["IdList"])
        # print("Term: ", self.record["TranslationStack"])
        if self.record["Count"] == "0" or self.record["IdList"]==[]:
            print ("não encontrado semelhantes")

        self.popResultWeb()


    def popResultWeb(self):
        self.pop = QMessageBox()
        self.pop.setWindowTitle("Resuldados")
        self.pop.setText("ID: "+ str(self.record["IdList"]) + "\n"  
            + "URL: " + self.handle.url +"\n"
            +"Número de bases: " + self.record["Count"] +"\n")
        # self.pop.setText(self.record["Count"])
        self.pop.setIcon(QMessageBox.Information)
        self.pop.exec_()

    def popResultLocal(self,handler):
        self.pop = QMessageBox()
        self.pop.setWindowTitle("Resuldados")
        self.pop.setText(handler)
        self.pop.setIcon(QMessageBox.Information)
        self.pop.exec_()

    def popError(self,file):
        self.pop = QMessageBox()
        self.pop.setWindowTitle("Erro")
        self.pop.setText("Formato errado")
        self.pop.setIcon(QMessageBox.Critical)
        self.pop.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MethodWindow = QtWidgets.QMainWindow()
    ui = Ui_MethodWindow()
    ui.setupUi(MethodWindow)
    MethodWindow.show()
    sys.exit(app.exec_())
