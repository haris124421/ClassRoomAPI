'''
Created on 16-Sep-2021

@author: muhammad.haris
'''
from PyQt5 import QtWidgets, QtGui, QtCore


class ClassRoomAPI(QtWidgets.QWidget):
   
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("ClassRoom API")
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\muhammad.haris\\Pictures\\rainbow-logo-210x210.png"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = ClassRoomAPI()
    myapp.show()
    sys.exit(app.exec_())