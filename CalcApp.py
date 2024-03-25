from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CalcUI(QtWidgets.QMainWindow):
    def __init__(self):
        '''constructor method'''
        super(CalcUI, self).__init__()
        uic.loadUi('/Users/tomknight/GUI-CalculatorA/GUI-Calculator/calc_window.ui',self)

        #add button event listeners here
        #self.Equalbutton.clicked.connect(self.btnInput())
        #self.Clearbutton.clicked.connect(self.btnInput())
        #self.Additionbutton.clicked.connect(self.btnInput())
        #self.Subtractbutton.clicked.connect(self.btnInput())
        #self.Multiplybutton.clicked.connect(self.btnInput())
        #self.Divisionbutton.clicked.connect(self.btnInput())
        #self.DecimaPoint.clicked.connect(self.btnInput())
        self.Zerobutton.clicked.connect(lambda: self.btnInput('0'))
        self.Onebutton.clicked.connect(lambda: self.btnInput('1'))
        self.Twobutton.clicked.connect(lambda: self.btnInput('2'))
        self.Threebutton.clicked.connect(lambda: self.btnInput('3'))
        self.Fourbutton.clicked.connect(lambda: self.btnInput('4'))
        self.Fivebutton.clicked.connect(lambda: self.btnInput('5'))
        self.Sixbutton.clicked.connect(lambda: self.btnInput('6'))
        self.Sevenbutton.clicked.connect(lambda: self.btnInput('7'))
        self.Eightbutton.clicked.connect(lambda: self.btnInput('8'))
        self.Ninebutton.clicked.connect(lambda: self.btnInput('9'))
        
        self.show()

    def btnInput(self, param):
        '''handles a button click'''
        self.current = self.current+str(param)
        #self.Outputlabel.setText(self.current)
        print(self.current)

    
def mainApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = CalcUI()
    app.exec_()
    app.quit() #quit when all windows are closed
    sys.exit(app.exec_()) #execute the application event loop

mainApplication()