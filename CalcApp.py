from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CalcUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        '''constructor method'''
        super(CalcUI, self).__init__()
        uic.loadUi('/Users/tomknight/GUI-CalculatorA/GUI-Calculator/calc_window.ui',self)
        self.display = ''
        self.current = ''
        #add button event listeners here
        self.Equalbutton.clicked.connect(self.equalMethod)
        self.Clearbutton.clicked.connect(self.allClearMethod)
        self.Adittionbutton.clicked.connect(lambda: self.opButton('+'))
        self.Adittionbutton.clicked.connect( self.OutputLblClear)
        self.Subtractbutton.clicked.connect(lambda: self.opButton('-'))
        self.Subtractbutton.clicked.connect(self.OutputLblClear)
        self.Multiplybutton.clicked.connect(lambda: self.opButton('*'))
        self.Multiplybutton.clicked.connect(self.OutputLblClear)
        self.Divisionbutton.clicked.connect(lambda: self.opButton('/'))
        self.Divisionbutton.clicked.connect(self.OutputLblClear)
        self.DecimalPoint.clicked.connect(lambda: self.btnInput('.'))
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
        self.Outputlabel.setAlignment(QtCore.Qt.AlignRight)
        self.show()

    def equalMethod(self):
        '''handles the euals operation'''
        self.current = str(eval(self.display))
        self.Outputlabel.setText(self.current)
        self.display = ''
        self.CalcOut.setText('')

    def btnInput(self, param):
        '''handles a button click'''
        self.current = self.current+str(param)
        self.Outputlabel.setText(self.current)
        self.display = self.display+str(param)
        self.CalcOut.setText(self.display)

    def allClearMethod(self):
        '''resets the display'''
        self.current = ''
        self.Outputlabel.setText('0')
        self.display = ''
        self.CalcOut.setText(self.display)
    
    def opButton(self, op):
        '''handles operators +,-,/,*'''
        self.display = self.display+str(op)
        self.CalcOut.setText(self.display)

    def OutputLblClear(self):
        '''clears the output label when an operator is called'''
        self.current = ''
        self.Outputlabel.setText('')

def mainApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = CalcUI()
    app.exec_()
    app.quit() #quit when all windows are closed
    sys.exit(app.exec_()) #execute the application event loop

mainApplication()