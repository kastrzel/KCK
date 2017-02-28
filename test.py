# -*- coding: utf-8 -*-
import aiml
import sys
import gtts
from pydub import AudioSegment
from pydub.playback import play
from PyQt5 import QtWidgets, QtCore, QtGui

debugMode = True
rachunek = 0
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        # self.setFixedSize(250,220)
        self.list = QtWidgets.QListWidget(self)
        self.speak = QtWidgets.QPushButton('Mów')
        self.answer = QtWidgets.QLabel('Tu pojawi sie odpowiedź.')
        self.order = QtWidgets.QLabel('Zamówienie nie zostało jeszcze złozone.')
        self.imagelabel = QtWidgets.QLabel()
        self.menulabel = QtWidgets.QLabel()
        self.isFemale = QtWidgets.QCheckBox("Kobieta")
        self.isOrderComplete = QtWidgets.QCheckBox("Zamówienie złożone")

        self.textInput = QtWidgets.QLineEdit()
        self.textInput.setPlaceholderText("Co chcesz powiedzieć?")
        self.textInput.setToolTip("Wpisz to co chcesz powiedzieć kelnerce.")
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.isFemale) #kobieta
        h_box.addWidget(self.order) #rachunek

        main_box = QtWidgets.QHBoxLayout()
        main_box.addWidget(self.menulabel)
        main_box.addWidget(self.list)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(main_box)  # image
        v_box.addWidget(self.answer)  # text
        v_box.addWidget(self.textInput)  # textinput
        v_box.addWidget(self.speak)  # button
        v_box.addLayout(h_box) # takie tam checkboxy

        self.setLayout(v_box)
        self.setWindowTitle('Kelner v 0.5')

        self.answer.setMargin(0)
        self.answer.setIndent(0)

        self.speak.clicked.connect(self.btn_click)

        #app_X = 250
        #app_Y = 250
        #screenGeo = QtWidgets.QDesktopWidget().screenGeometry().center()

        #self.move((screenGeo.width() / 2) - (self.frameGeometry().width() / 4),(screenGeo.height() / 2) - (self.frameGeometry().height() / 2))
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 4),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        self.answer.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.order.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelabel.setPixmap(QtGui.QPixmap('kelner.png'))
        self.menulabel.setPixmap(QtGui.QPixmap('menu.png'))
        # print(screen_X)

        self.show()

    def btn_click(self):
        global rachunek
        sentence = self.textInput.text().replace("ą","a").replace("ć","c").replace("ę","e").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ż","z").replace("ź","z").replace("schabowego","schabowy").replace("z frytkami","").replace("i buraczkami","").replace("z ziemniakami","").replace("z kapusta kiszona","").replace("w sosie","").replace("pomidorowym z ryzem","").replace("z ryzem","").replace("z makaronem","").replace("czerwony","").replace("z pasztecikiem","").replace("z owocami","").replace("i polewa","").replace("na cieplo","").replace("z bita smietana","").replace("z salsa","").replace("z kurczakiem","").replace("fante","fanta").replace("z czarnej porzeczki","porzeczkowy").replace("wode","woda").replace("mineralna","")
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
        
        if (k.getPredicate("rachunek") == "no"):
            response = k.respond(sentence.strip(",."))
            if debugMode:
                print(response)
            self.answer.setText("Kelner: " + response)

            if (k.getPredicate("order") != ""):
                self.list.addItem(k.getPredicate("order") + " - " + k.getPredicate("cena") + "zł")
                rachunek += int(k.getPredicate("cena"))
                k.setPredicate("order", "")
                k.setPredicate("cena", "")
                self.order.setText("Rachunek: " + str(rachunek) + "zł")


        app.processEvents()
        #if response:
        #   self.playsound(response)




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
k.loadSubs("sets/zupy.set")
k.setPredicate("plec", "m")
k.setPredicate("hello", "n")
k.setPredicate("napoj", "no")
k.setPredicate("danie", "")
k.setPredicate("rachunek","no")

'''from bottle import route, run, static_file, view, url, template, request


@route('/')
def index():
    return template('index', test=("tu pojawi sie odpowiedz"))

@route('/', method='POST')
def test():
    question = request.forms.get('question')
    return template('index', test=(request.forms.get('question')))

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080, debug=True)'''


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
