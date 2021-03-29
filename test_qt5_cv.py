import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout ,QLabel,QGridLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap,QFont
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot
import cv2
from shrim_color_capture import *
import numpy as np
from collections import Counter
import RPi.GPIO as GPIO



Led_white = 37

GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)


GPIO.setup(Led_white, GPIO.OUT)


GPIO.output(Led_white, GPIO.LOW)




class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'VietUc Shrimp color Indexing'
        self.left = 0
        self.top = 0
        self.width = 1920
        self.height = 1080
        # self.label_main = QLabel()
        self.image_frame = QtWidgets.QLabel() 
        self.initUI()
        self.trai = None
        self.ao = None
        self.led_flag = 0
        self.value = 0
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: white;") 
        # self.label.setStyleSheet("border: 1px solid black;")
        self.setFixedSize(self.width,self.height)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        
        # self.setWindowIcon(QIcon('logo_VU.png'))
        
        self.createHorizontalLayout()
        


        windowLayout = QGridLayout()
        #windowLayout.setSpacing(2)
        
        

        
        pixmap = QPixmap('/home/pi/chat_luong_tom/rsz_bg.jpg')
        self.image_frame.setPixmap(pixmap)
        self.image_frame.setFixedSize(int(self.width/1.5),int(self.height/1.5))
        #label_main.setFixedWidth(1312)
        #label_main.setFixedHeight(900)
        #label_main.setGeometry(10,140,1312,900)
        #label_main.move(10,140)
        #label_main.resize(1312,900)
        

        self.label_1 = QLabel("Trai - Ao", self) 
        self.label_1.setStyleSheet('color: lightblue')
        self.label_1.setFixedSize(int(self.width/6.4),int(self.height/18))
        #self.label_1.setFixedWidth(300)
        #self.label_1.setFixedHeight(300)
        #self.label_1.setGeometry(1500,720,300,300)
        #self.label_1.move(1500, 850)
        self.label_1.setFont(QFont('Arial', 30))
        


        self.label_2 = QLabel("Gia Tri Dem Trung Binh", self) 
        self.label_2.setStyleSheet('color: lightblue')
        self.label_2.setFixedSize(int(self.width/1.5),int(self.height/18))
        #self.label_2.setGeometry(1370,820,600,300)
        #self.label_1.move(1500, 850)
        self.label_2.setFont(QFont('Arial', 30))
        




        label = QLabel(self)
        pixmap = QPixmap('/home/pi/chat_luong_tom/rsz_logo_vu.png')
        label.setPixmap(pixmap)
        label.setFixedSize(int(self.width/3.5),int(self.width/3.5))
        #label.setGeometry(1350,210,600,600)
        #label.move(1350,210)
        label.resize(600,600)


        # Text_label = QLabel(" VIETUC SHRIMP COLOR INDEXING ")
        # Text_label.setFont(QFont('Arial', 25))
        # Text_label.setStyleSheet('color: red')
        


        windowLayout.addWidget(self.horizontalGroupBox,0,0)
        #windowLayout.addWidget(Text_label,0,1)
        #windowLayout.addWidget(self.image_frame,1,0)
        #windowLayout.addWidget(self.label_main,1,0)
        windowLayout.addWidget(self.image_frame,1,0)
        windowLayout.addWidget(label,1,1)
        windowLayout.addWidget(self.label_1,2,1)
        windowLayout.addWidget(self.label_2,2,0)

        self.setLayout(windowLayout)                                                                                                
        #self.setStyleSheet("background-color: white;") 
        self.show()
        
    
    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox()
        ##self.horizontalGroupBox.setGeometry(10,10,1312,990)
        self.horizontalGroupBox.setFixedSize(int(self.width/1.5),100)
        self.horizontalGroupBox.move(10,10)
        self.horizontalGroupBox.setStyleSheet("background-color: white;border: none;")
        layout = QHBoxLayout()
        
        buttoncapture = QPushButton('Capture', self)
        buttoncapture.setStyleSheet("background-color: green;border: none;")
        buttoncapture.setMaximumHeight(90)
        buttoncapture.clicked.connect(self.getText)
        layout.addWidget(buttoncapture)
        
        self.buttonLedOn = QPushButton('Led Control', self)
        self.buttonLedOn.setCheckable(True)
        self.buttonLedOn.clicked.connect(self.led_control)
        self.buttonLedOn.setMaximumHeight(90)
        layout.addWidget(self.buttonLedOn)


        buttonShutdown = QPushButton('Shutdown', self)
        buttonShutdown.setStyleSheet("background-color: red;border: none;")
        buttonShutdown.clicked.connect(self.shutdown)
        buttonShutdown.setMaximumHeight(90)
        layout.addWidget(buttonShutdown)
        

        
        self.horizontalGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def show_image(self):
        if not (self.trai == "") and not(self.ao == "") :
            self.image,self.value = color_index(self.trai,self.ao)
            self.image = cv2.resize(self.image,(int(self.width/1.5),int(self.height/1.2)))
            #print("self.value = ",self.value)
            self.label_1.setText("Trai: " + str(self.trai) + " , " + "Ao: " + str(self.ao))
            if len(self.value) > 1:
                self.label_2.setText(str(Counter(self.value)) + " - " " Gia Tri Dem Trung Binh: " + str(int(round(np.mean(self.value)))))
            else:
                pass
            self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
            self.image_frame.setFixedSize(1280,700)
        else:
            pass
    def shutdown(self):
        print("shutting down")
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        import subprocess
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)
    def led_control(self):
        if self.buttonLedOn.isChecked():
            self.buttonLedOn.setStyleSheet("background-color: yellow;border: none;")
            self.buttonLedOn.setText("LED ON")
            GPIO.output(Led_white, GPIO.HIGH)
            print("led on")
        else:
            self.buttonLedOn.setStyleSheet("background-color: white;border: none;")
            self.buttonLedOn.setText("LED OFF")
            GPIO.output(Led_white, GPIO.LOW)
            print("led off")
    def getText(self):
        trai = QInputDialog(self)
        trai.setWindowTitle("TRAI")
        trai.setInputMode( QInputDialog.TextInput) 
        trai.setLabelText("NHAP VAO SO TRAI")
        trai.setFixedSize(440,280)
        trai.setFont(QFont('Arial', 50))
        okPressed = trai.exec_()
        self.trai = trai.textValue()

        ao = QInputDialog(self)
        ao.setInputMode( QInputDialog.TextInput) 
        trai.setWindowTitle("TRAI")
        ao.setLabelText("NHAP VAO SO AO")
        ao.setFont(QFont('Arial', 50))
        ao.setFixedSize(440,280)
        okPressed = ao.exec_()
        self.ao = ao.textValue()
        #self.trai, okPressed_ = QInputDialog.getText(self, "Get text","Trai:", QLineEdit.Normal, "")
        #self.ao, okPressed = QInputDialog.getText(self, "Get text","Ao:", QLineEdit.Normal, "")
        #if self.ao != '' and self.trai != '':
            #print(trai +"-" + Ao)
        #print(self.trai == "")
        
        self.show_image()
        #else:
        #    pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
