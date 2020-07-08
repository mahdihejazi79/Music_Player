import os, sys, time
import PyQt5.QtWidgets
import PyQt5.QtGui
import threading
from pygame.mixer import init, music

#GLOBAL VARIABLES
#"sample.wav" can be changed.
m = "sample.mp3"
timeStarted = 0
timePassed = 0

class Example(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('SansSerif', 10))

        btnPlay = PyQt5.QtWidgets.QPushButton('', self)
        btnPlay.setIcon(PyQt5.QtGui.QIcon('logoPlay.png'))
        btnPlay.clicked.connect(self.Play)
        btnPlay.resize(20, 20)
        btnPlay.move(50, 50)

        btnPause = PyQt5.QtWidgets.QPushButton('', self)
        btnPause.setIcon(PyQt5.QtGui.QIcon('logoPause.png'))
        btnPause.clicked.connect(self.Pause)
        btnPause.resize(20, 20)
        btnPause.move(80, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def Play(self):
        init(44100, -16,2,2048)
        global timeStarted, timePassed, m
        if not os.path.isfile(m):
            print("File doesn't exist!")
        elif m.endswith('.mp3'):
            music.load(m)
            music.play(0, timePassed)
            timeStarted = time.time()
        #in .wav files, we should start playiny from the begining
        elif m.endswith('.wav'):
            music.load(m)
            music.play()
        else:
            print("Music file can't be played!")
        
    def Pause(self):
        music.pause()
        global timePassed
        timePassed += time.time() - timeStarted

def f():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    f()