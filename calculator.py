from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainUI():
    def setupUi(self, MainWindow):
        self.tail = "0"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 390)
        MainWindow.setMinimumSize(QtCore.QSize(321, 399))
        MainWindow.setMaximumSize(QtCore.QSize(321, 399))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 220, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 220, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 220, 61, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 61, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 170, 61, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 170, 61, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 120, 61, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 120, 61, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 120, 61, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 120, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(250, 170, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(250, 270, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(250, 320, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 270, 61, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 270, 61, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 0, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setMaxLength(9)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(250, 70, 61, 41))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.clearall)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.zero)
        self.pushButton_2.clicked.connect(self.one)
        self.pushButton_3.clicked.connect(self.two)
        self.pushButton_4.clicked.connect(self.three)
        self.pushButton_5.clicked.connect(self.four)
        self.pushButton_6.clicked.connect(self.five)
        self.pushButton_7.clicked.connect(self.six)
        self.pushButton_8.clicked.connect(self.seven)
        self.pushButton_9.clicked.connect(self.eight)
        self.pushButton_10.clicked.connect(self.nine)
        self.pushButton_11.clicked.connect(self.divide)
        self.pushButton_12.clicked.connect(self.multiply)
        self.pushButton_13.clicked.connect(self.minus)
        self.pushButton_14.clicked.connect(self.plus)
        self.pushButton_15.clicked.connect(self.calculate)
        self.pushButton_16.clicked.connect(self.fpoint)
        self.pushButton_17.clicked.connect(self.chsign)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_11.setText(_translate("MainWindow", "/"))
        self.pushButton_12.setText(_translate("MainWindow", "X"))
        self.pushButton_13.setText(_translate("MainWindow", "-"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.pushButton_16.setText(_translate("MainWindow", "."))
        self.pushButton_17.setText(_translate("MainWindow", "+/-"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.pushButton_18.setText(_translate("MainWindow", "Clear"))

    def zero(self):
        if self.tail == "0":
            self.tail = "0"
        else:
            self.tail = self.tail + "0"
        self.lineEdit.setText(self.tail)

    def one(self):
        if self.tail == "0":
            self.tail = "1"
        else:
            self.tail = self.tail + "1"
        self.lineEdit.setText(self.tail)

    def two(self):
        if self.tail == "0":
            self.tail = "2"
        else:
            self.tail = self.tail + "2"
        self.lineEdit.setText(self.tail)

    def three(self):
        if self.tail == "0":
            self.tail = "3"
        else:
            self.tail = self.tail + "3"
        self.lineEdit.setText(self.tail)

    def four(self):
        if self.tail == "0":
            self.tail = "4"
        else:
            self.tail = self.tail + "4"
        self.lineEdit.setText(self.tail)

    def five(self):
        if self.tail == "0":
            self.tail = "5"
        else:
            self.tail = self.tail + "5"
        self.lineEdit.setText(self.tail)

    def six(self):
        if self.tail == "0":
            self.tail = "6"
        else:
            self.tail = self.tail + "6"
        self.lineEdit.setText(self.tail)

    def seven(self):
        if self.tail == "0":
            self.tail = "7"
        else:
            self.tail = self.tail + "7"
        self.lineEdit.setText(self.tail)

    def eight(self):
        if self.tail == "0":
            self.tail = "8"
        else:
            self.tail = self.tail + "8"
        self.lineEdit.setText(self.tail)

    def nine(self):
        if self.tail == "0":
            self.tail = "9"
        else:
            self.tail = self.tail + "9"
        self.lineEdit.setText(self.tail)

    def plus(self):
        if self.tail != "0" and "+" not in self.tail:
            self.tail = self.tail + "+"
        self.lineEdit.setText(self.tail)

    def minus(self):
        if self.tail != "0" and "-" not in self.tail:
            self.tail = self.tail + "-"
        self.lineEdit.setText(self.tail)

    def divide(self):
        if self.tail != "0" and "/" not in self.tail:
            self.tail = self.tail + "/"
        self.lineEdit.setText(self.tail)

    def multiply(self):
        if self.tail != "0" and "*" not in self.tail:
            self.tail = self.tail + "*"
        self.lineEdit.setText(self.tail)

    def fpoint(self):
        if ".." in self.tail:
            rawstring = self.tail
            propstring = rawstring.replace("..", ".")
            self.lineEdit.setText(propstring)
        self.tail = self.tail + "."
        self.lineEdit.setText(self.tail)

    def calculate(self):
        rawstring = self.tail
        propstring = rawstring.replace("x", "*")
        eq = eval(propstring)
        self.lineEdit.setText(str(eq))
        self.tail = str(eq)

    def clearall(self):
        self.tail = "0"
        self.lineEdit.setText(self.tail)

    def chsign(self):
        char = self.tail
        char = eval(char) - 2 * eval(char)
        self.tail = str(char)
        self.lineEdit.setText(str(self.tail))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainui = MainUI()
    mainui.setupUi(MainWindow)
    mainui.retranslateUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
