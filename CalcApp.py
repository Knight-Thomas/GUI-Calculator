from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CalcUI(QtWidgets.QMainWindow):
    def __init__(self):
        '''constructor method'''
        super(CalcUI, self).__init__
        uic.loadUi('calc_window.ui',self)

        #add button event listeners here

        self.show()
    
def mainApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = CalcUI()
    app._exec_()
    app.quit() #quit when all windows are closed
    sys.exit(app.exec_()) #execute the application event loop