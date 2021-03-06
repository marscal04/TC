# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methodWindow.ui'
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
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMaximumSize(QtCore.QSize(500, 400))

        self.methodLabel = QtWidgets.QLabel(Form)
        self.methodLabel.setGeometry(QtCore.QRect(190, 20, 158, 24))
        font = QtGui.QFont()
        font.setPointSize(15)

        self.methodLabel.setFont(font)
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodLabel.setObjectName("methodLabel")

        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(40, 70, 441, 301))
        self.toolBox.setObjectName("toolBox")

        self.pesquisar = QtWidgets.QWidget()
        self.pesquisar.setGeometry(QtCore.QRect(0, 0, 431, 237))
        self.pesquisar.setObjectName("pesquisar")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pesquisar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.frame_2 = QtWidgets.QFrame(self.pesquisar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.nameLine = QtWidgets.QLineEdit(self.frame_2)
        self.nameLine.setObjectName("nameLine")

        self.gridLayout_5.addWidget(self.nameLine, 0, 0, 1, 1)

        self.nameCheck = QtWidgets.QCheckBox(self.frame_2)
        self.nameCheck.setObjectName("nameCheck")

        self.gridLayout_5.addWidget(self.nameCheck, 0, 1, 1, 1)

        self.genLine = QtWidgets.QLineEdit(self.frame_2)
        self.genLine.setObjectName("genLine")

        self.gridLayout_5.addWidget(self.genLine, 1, 0, 1, 1)

        self.genCheck = QtWidgets.QCheckBox(self.frame_2)
        self.genCheck.setObjectName("genCheck")

        self.gridLayout_5.addWidget(self.genCheck, 1, 1, 1, 1)

        self.idLine = QtWidgets.QLineEdit(self.frame_2)
        self.idLine.setObjectName("idLine")

        self.gridLayout_5.addWidget(self.idLine, 2, 0, 1, 1)

        self.idCheck = QtWidgets.QCheckBox(self.frame_2)
        self.idCheck.setObjectName("idCheck")

        self.gridLayout_5.addWidget(self.idCheck, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.toolBox.addItem(self.pesquisar, "")

        self.inserir = QtWidgets.QWidget()
        self.inserir.setGeometry(QtCore.QRect(0, 0, 441, 247))
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

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Quando o estado do CheckBox muda
        # Vai para a função isButtonCheck()
        self.nameCheck.stateChanged.connect(lambda:self.isButtonChecked(self.nameCheck))
        self.idCheck.stateChanged.connect(lambda:self.isButtonChecked(self.idCheck))
        self.genCheck.stateChanged.connect(lambda:self.isButtonChecked(self.genCheck))

        self.email = Entrez.email = 'gabrielgmusskopf@gmail.com'


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.methodLabel.setText(_translate("Form", "Escolha o método"))
        self.nameCheck.setText(_translate("Form", "Nome"))
        self.genCheck.setText(_translate("Form", "Gene"))
        self.idCheck.setText(_translate("Form", "ID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pesquisar), _translate("Form", "Pesquisar"))
        self.fileButton.setText(_translate("Form", "Procurar"))
        self.seqLabel.setText(_translate("Form", "ou digitar a sequência"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.inserir), _translate("Form", "Inserir"))

        # Quando botão é clicado, vai para a função fileBrowser()
        self.fileButton.clicked.connect(self.fileBrowser) 

        

    def fileBrowser(self):
        print ("button pressed")
        self.openDialogBox()

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName(filter="Fasta files (*.fasta)")
        path = filename[0]
        print(path)

        file = open(path,"r")
        print(file.read())


    def isButtonChecked(self, b):
    # Verifica qual o botão
    # Verifica se está marcado
    # Verifica se é nulo
    # Vai para função de busca do botão específico

        if b.text() == "Nome":
            if b.isChecked() == True:
                if self.nameLine.text() != "":
                    print (b.text()+" is selected")
                    self.search(self.nameLine)

                
        if b.text() == "Gene":
            if b.isChecked() == True:
                if self.genLine.text() != "":
                    print (b.text()+" is selected")
                    self.search(self.genLine)


        if b.text() == "ID":
            if b.isChecked() == True:
                if self.idLine.text() != "":
                    print (b.text()+" is selected")
                    self.search(self.idLine)
            


    def search(self, line):
        # print (line.text())
        

        # handle = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", rettype = "fasta", retmode = "text", idtype="acc") 
        # record = Entrez.read(handle)
        handle = Entrez.esearch(db="nucleotide", term = line.text(), idtype="acc", retmax = 1) 
        record = Entrez.read(handle) #lendo as infos geradas pela pesquisa
        handle.close()


        print (handle.url)
        
        print(record["Count"])
        print("ID List: ", record["IdList"])

        # print (record.seq)
        print(line.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
