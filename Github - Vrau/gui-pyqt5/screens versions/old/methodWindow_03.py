# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'methodWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import Bio
from Bio import Entrez  #  Importar módulo Bio.Entrez 
from Bio import SeqIO   #   Módulo para analisar sequências
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys
import loginWindow_02



class Ui_MethodWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.gridLayout_6 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.methodLabel = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.methodLabel.setFont(font)
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodLabel.setObjectName("methodLabel")
        self.gridLayout_6.addWidget(self.methodLabel, 0, 0, 1, 1)
        self.toolBox = QtWidgets.QToolBox(MainWindow)
        self.toolBox.setObjectName("toolBox")
        self.pesquisar = QtWidgets.QWidget()
        self.pesquisar.setGeometry(QtCore.QRect(0, 0, 482, 298))
        self.pesquisar.setObjectName("pesquisar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pesquisar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.pesquisar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.searchLabel = QtWidgets.QLabel(self.frame_2)
        self.searchLabel.setGeometry(QtCore.QRect(90, 40, 285, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")
        self.searchText = QtWidgets.QLineEdit(self.frame_2)
        self.searchText.setGeometry(QtCore.QRect(20, 80, 421, 71))
        self.searchText.setObjectName("searchText")
        self.searchButton = QtWidgets.QPushButton(self.frame_2)
        self.searchButton.setGeometry(QtCore.QRect(180, 170, 101, 31))
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.toolBox.addItem(self.pesquisar, "")
        self.inserir = QtWidgets.QWidget()
        self.inserir.setGeometry(QtCore.QRect(0, 0, 482, 298))
        self.inserir.setObjectName("inserir")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inserir)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.inserir)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fileName = QtWidgets.QLabel(self.frame)
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.gridLayout_4.addWidget(self.fileName, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileLabel = QtWidgets.QLineEdit(self.frame)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout.addWidget(self.fileLabel)
        self.fileButton = QtWidgets.QPushButton(self.frame)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout.addWidget(self.fileButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.seqLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seqLabel.setFont(font)
        self.seqLabel.setObjectName("seqLabel")
        self.verticalLayout.addWidget(self.seqLabel)
        self.seqPlainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.seqPlainTextEdit.setObjectName("seqPlainTextEdit")
        self.verticalLayout.addWidget(self.seqPlainTextEdit)
        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.toolBox.addItem(self.inserir, "")
        self.gridLayout_6.addWidget(self.toolBox, 1, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # InMainWindowando o email do usuário
        self.email = Entrez.email = "gabrielgmusskopf@gmail.com"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.methodLabel.setText(_translate("MainWindow", "Escolha o método"))
        self.searchLabel.setText(_translate("MainWindow", "Insira o nome, ID ou sequência nucleotídica"))
        self.searchButton.setText(_translate("MainWindow", "OK"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pesquisar), _translate("MainWindow", "Pesquisar"))
        self.fileButton.setText(_translate("MainWindow", "Procurar"))
        self.seqLabel.setText(_translate("MainWindow", "ou digitar a sequência"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.inserir), _translate("MainWindow", "Inserir"))

        # Quando botão é clicado, vai para a função fileBrowser()
        self.fileButton.clicked.connect(self.fileBrowser) 
        # Quando botão de pesquisar, verifica se a pesquisa é válida
        self.searchButton.clicked.connect(self.isValidSearch)



    def fileBrowser(self):
        self.openDialogBox()
        # print ("button pressed")

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
        path = filename[0]
        print(path)

        file = open(path,"r")
        print(file.read())


    def isValidSearch(self):
    # Verifica se o texto é válido

        if self.searchText.text() != "":
            print (self.searchText.text())
            self.search()
        else:
            print('texto não válido')



    def search(self):
        handle = Entrez.esearch(db="nucleotide", term = self.searchText.text(), idtype="acc", retmax = 1) 
        record = Entrez.read(handle) #lendo as infos geradas pela pesquisa
        handle.close()

        print (handle.url)
        print(record["Count"])
        print("ID List: ", record["IdList"])

        if record["Count"] == "0" or record["IdList"]==[]:
            print ("não encontrado semelhantes")

    def screenPrint(self):
        print("foi")
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MethodWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
