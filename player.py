import sys
import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5.QtMultimedia import QSound
import time
import threading, playsound

# "strings.wav" should be changed
m = "strings.wav"

def Play():
    playsound.playsound(m)

t = threading.Thread(target=Play)

def BtnPlay():
    if t.is_alive(): 
        print('Still running')
    else: 
        print("Let's start")
        t.start()

class Example(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('SansSerif', 10))

        btnPlay = PyQt5.QtWidgets.QPushButton('play/stop', self)
        btnPlay.clicked.connect(BtnPlay)
        btnPlay.resize(btnPlay.sizeHint())
        btnPlay.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def f():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    f()