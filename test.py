import aiml
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

#from tkinter import *
#from PIL import ImageTk, Image

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        #self.setFixedSize(250,220)
        self.b = QtWidgets.QPushButton('Mów')
        self.l = QtWidgets.QLabel('Tu pojawi sie odpowiedź.')
        self.l2 = QtWidgets.QLabel()
        self.checkbox = QtWidgets.QCheckBox("Kobieta")

        self.textInput = QtWidgets.QLineEdit()
        self.textInput.setPlaceholderText("Co chcesz powiedzieć?")
        self.textInput.setToolTip("Wpisz to co chcesz powiedzieć papieżowi.")
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l) 
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.l2) #image
        v_box.addWidget(self.l) #text
        v_box.addWidget(self.textInput) #textinput
        v_box.addWidget(self.b) #button
        v_box.addWidget(self.checkbox) #taki tam checkbox

        self.setLayout(v_box)
        self.setWindowTitle('Kelner v 0.0.1')

        self.l.setMargin(0)
        self.l.setIndent(0)


        self.b.clicked.connect(self.btn_click)

        app_X = 250
        app_Y = 250
        screenGeo = QtWidgets.QDesktopWidget().screenGeometry()

        #self.setGeometry((screenGeo.width() / 2) - (app_X / 2),
                    #(screenGeo.height() / 2) - (app_Y / 2))
        self.l.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setPixmap(QtGui.QPixmap('kelner.png'))
        #print(screen_X)

        self.show()


    def btn_click(self):
        sentence = self.textInput.text()
        if self.checkbox.isChecked():
            k.setPredicate("plec", "k")
        else:
            k.setPredicate("plec", "m")
        self.l.setText("Kelner: " + k.respond(sentence))

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml")
k.loadSubs("sets/test.set")
k.setPredicate("plec", "m")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()

app_icon = QtGui.QIcon()
app_icon.addFile('kelner.png', QtCore.QSize(16,16))
app_icon.addFile('kelner.png', QtCore.QSize(24,24))
app_icon.addFile('kelner.png', QtCore.QSize(32,32))
app_icon.addFile('kelner.png', QtCore.QSize(48,48))
app_icon.addFile('kelner.png', QtCore.QSize(256,256))
app.setWindowIcon(app_icon)

sys.exit(app.exec_())
