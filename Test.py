
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_class = uic.loadUiType("uiTest_02.ui")[0]

class WindowMain(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #여기에 시그널, 설정
        print(__file__)

    #여기에 함수 설정




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowMain()
    myWindow.show()
    app.exec_()