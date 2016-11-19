import aiml
import sys
import gtts
from pydub import AudioSegment
from pydub.playback import play
from PyQt5 import QtWidgets, QtCore, QtGui

debugMode = True

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        # self.setFixedSize(250,220)
        self.speak = QtWidgets.QPushButton('Mów')
        self.answer = QtWidgets.QLabel('Tu pojawi sie odpowiedź.')
        self.imagelabel = QtWidgets.QLabel()
        self.isFemale = QtWidgets.QCheckBox("Kobieta")
        self.isOrderComplete = QtWidgets.QCheckBox("Zamówienie złożone")

        self.textInput = QtWidgets.QLineEdit()
        self.textInput.setPlaceholderText("Co chcesz powiedzieć?")
        self.textInput.setToolTip("Wpisz to co chcesz powiedzieć papieżowi.")
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.isFemale) #kobieta
        h_box.addWidget(self.isOrderComplete) #rachunek

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.imagelabel)  # image
        v_box.addWidget(self.answer)  # text
        v_box.addWidget(self.textInput)  # textinput
        v_box.addWidget(self.speak)  # button
        v_box.addLayout(h_box) # takie tam checkboxy

        self.setLayout(v_box)
        self.setWindowTitle('Kelner v 0.2-alpha')

        self.answer.setMargin(0)
        self.answer.setIndent(0)

        self.speak.clicked.connect(self.btn_click)

        app_X = 250
        app_Y = 250
        screenGeo = QtWidgets.QDesktopWidget().screenGeometry()

        # self.setGeometry((screenGeo.width() / 2) - (app_X / 2),
        #(screenGeo.height() / 2) - (app_Y / 2))
        self.answer.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelabel.setPixmap(QtGui.QPixmap('kelner.png'))
        # print(screen_X)

        self.show()

    def btn_click(self):
        sentence = self.textInput.text().replace("ą","a").replace("ć","c").replace("ę","e").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ż","z").replace("ź","z")
        #sentence = ''.join( c for c in sentence if c not in 'ąćęłńóśżź')
        if debugMode:
            print("Question: " + sentence)
        if self.isFemale.isChecked():
            k.setPredicate("plec", "k")
        else:
            k.setPredicate("plec", "m")

        if self.isOrderComplete.isChecked():
            k.setPredicate("rachunek", "yes")
        else:
            k.setPredicate("rachunek", "no")
        
        response = k.respond(sentence.strip(",."))
        self.answer.setText("Kelner: " + response)
        app.processEvents()
        if response:
            self.playsound(response)




    def playsound(self, response):
        response_strip=response.replace(",","").lower()
        if debugMode:
            print("TTS response: " + response_strip)
        tts = gtts.gTTS(text=response_strip, lang='pl')
        tts.save("kelner.mp3")
        song = AudioSegment.from_mp3("kelner.mp3")
        play(song)


k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml")
k.loadSubs("sets/test.set")
k.setPredicate("plec", "m")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()

app_icon = QtGui.QIcon()
app_icon.addFile('kelner.png', QtCore.QSize(16, 16))
app_icon.addFile('kelner.png', QtCore.QSize(24, 24))
app_icon.addFile('kelner.png', QtCore.QSize(32, 32))
app_icon.addFile('kelner.png', QtCore.QSize(48, 48))
app_icon.addFile('kelner.png', QtCore.QSize(256, 256))
app.setWindowIcon(app_icon)

sys.exit(app.exec_())