import sys
import os
#import telepot
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, QRect
from subprocess import Popen, PIPE


motionText = "motion disabled"

class Horus(object):

    def __init__(self):
        super(Horus, self).__init__()
        self.initUI()

    def initUI(self):
        self.w = QWidget()
        self.w.resize(320,240)
        self.w.setWindowTitle("Horus Project")
        self.w.setAutoFillBackground(True)
        self.pbackground = self.w.palette()
        self.pbackground.setColor(self.w.backgroundRole(), Qt.white)
        self.w.setPalette(self.pbackground)
        
        self.myBanner = QLabel()
        self.myBanner.setFixedSize(320,50)
        self.myBanner.setStyleSheet("background-color: #ab963d")
        self.myBanner.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap('eye.png')
        self.myBanner.setPixmap(self.pixmap)

        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0,0,0,0)
        self.vbox.addWidget(self.myBanner)
        
        self.buttonLayout = QHBoxLayout()
        self.buttonActivateSystems = QPushButton("Activar")
        self.buttonActivateSystems.setStyleSheet("background-color: #d6caa0;""border-style: outset;")
        self.buttonActivateSystems.setFixedSize(117,34)
        self.buttonLayout.setContentsMargins(0,20,0,0)
        self.buttonActivateSystems.clicked.connect(self.activateSystems)
        self.buttonLayout.addWidget(self.buttonActivateSystems)
        
        self.motionAntenaLayout = QHBoxLayout()
        self.motionLabel = QLabel()
        self.motionPixmap = QPixmap('webcam.png')
        self.motionLabel.setPixmap(self.motionPixmap)
        self.motionLabel.setContentsMargins(0,0,25,0)
        self.antenaLabel = QLabel()
        self.antenaPixmap = QPixmap('antena.png')
        self.antenaLabel.setPixmap(self.antenaPixmap)
        self.antenaLabel.setContentsMargins(25,0,0,0)
        self.motionAntenaLayout.addWidget(self.motionLabel)
        self.motionAntenaLayout.addWidget(self.antenaLabel)
        self.motionAntenaLayout.setContentsMargins(0,15,0,0)
        self.motionAntenaLayout.setAlignment(Qt.AlignCenter)

        self.motionAntenaInfoLayout = QHBoxLayout()
        self.motionInfoLabel = QLabel()
        self.motionInfoLabel.setText(motionText)
        self.motionInfoLabel.setStyleSheet("color:red")
        self.motionInfoLabel.setContentsMargins(0,0,25,0)
        self.antenaInfoLabel = QLabel()
        self.antenaInfoLabel.setText("update public ip")
        self.antenaInfoLabel.setContentsMargins(15,0,0,0)
        self.antenaInfoLabel.setStyleSheet("color:red")
        self.motionAntenaInfoLayout.addWidget(self.motionInfoLabel)
        self.motionAntenaInfoLayout.addWidget(self.antenaInfoLabel)
        self.motionAntenaInfoLayout.setContentsMargins(0,5,0,0)
        self.motionAntenaInfoLayout.setAlignment(Qt.AlignCenter)

        self.vbox.addLayout(self.buttonLayout)
        self.vbox.addLayout(self.motionAntenaLayout)
        self.vbox.addLayout(self.motionAntenaInfoLayout)
        self.vbox.addStretch()
        
        self.w.setLayout(self.vbox)
        
        self.w.show()

    def motionActivate(self):
        #os.system('sudo motion start')
        result = Popen(['sudo','motion','start'], stdin=PIPE, stderr=PIPE,universal_newlines=True)
        if result.returncode == 0:
            self.motionInfoLabel.setText("motion enabled")
            self.motionInfoLabel.setStyleSheet("color:green")
            return True


    def noIp2Update(self):
        os.system('sudo /usr/local/bin/noip2')
        self.antenaInfoLabel.setText("public ip is update")
        self.antenaInfoLabel.setStyleSheet("color:green")

    def activateSystems(self):
        self.motionActivate()
        self.noIp2Update()
        #bot = telepot.Bot()
        bot.sendMessage(644040082,"sistema activado")
    
        
def main():
    app = QApplication(sys.argv)
    horus = Horus()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
