# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/StartingUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 760)
        MainWindow.setMinimumSize(QtCore.QSize(560, 760))
        MainWindow.setMaximumSize(QtCore.QSize(560, 760))
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #3c3c3c")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 561, 211))
        self.frame.setStyleSheet("background-color: #d70007")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.typing_test = QtWidgets.QLabel(self.frame)
        self.typing_test.setGeometry(QtCore.QRect(80, 20, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.typing_test.setFont(font)
        self.typing_test.setStyleSheet("color: #FFFFFF")
        self.typing_test.setObjectName("typing_test")
        self.time_bar = QtWidgets.QProgressBar(self.frame)
        self.time_bar.setGeometry(QtCore.QRect(0, 190, 601, 23))
        self.time_bar.setProperty("value", 24)
        self.time_bar.setObjectName("time_bar")
        self.textInterface = QtWidgets.QTextBrowser(self.centralwidget)
        self.textInterface.setGeometry(QtCore.QRect(30, 240, 511, 241))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textInterface.setFont(font)
        self.textInterface.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textInterface.setStyleSheet("border: 2px solid #0d0718;\n"
"border-radius: 5px;\n"
"color: #989898")
        self.textInterface.setObjectName("textInterface")
        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(30, 490, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.speed.setFont(font)
        self.speed.setStyleSheet("background-color: #d70007;\n"
"border: 2px solid #d70007;\n"
"border-radius: 30px;\n"
"color: white")
        self.speed.setObjectName("speed")
        self.mistakes = QtWidgets.QLabel(self.centralwidget)
        self.mistakes.setGeometry(QtCore.QRect(290, 490, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mistakes.setFont(font)
        self.mistakes.setStyleSheet("background-color: #d70007;\n"
"border: 2px solid #d70007;\n"
"border-radius: 30px;\n"
"color: white")
        self.mistakes.setObjectName("mistakes")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 570, 561, 191))
        self.frame_2.setStyleSheet("background-color: #388c18")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.crown = QtWidgets.QLabel(self.frame_2)
        self.crown.setGeometry(QtCore.QRect(20, 50, 141, 81))
        self.crown.setText("")
        self.crown.setPixmap(QtGui.QPixmap("data\\Crown.png"))
        self.crown.setObjectName("crown")
        self.best_record = QtWidgets.QLabel(self.frame_2)
        self.best_record.setGeometry(QtCore.QRect(180, 20, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.best_record.setFont(font)
        self.best_record.setStyleSheet("color: white")
        self.best_record.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.best_record.setLineWidth(2)
        self.best_record.setObjectName("best_record")
        self.record = QtWidgets.QLabel(self.frame_2)
        self.record.setGeometry(QtCore.QRect(180, 60, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.record.setFont(font)
        self.record.setStyleSheet("color: white;")
        self.record.setText("")
        self.record.setObjectName("record")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.typing_test.setText(_translate("MainWindow", "Typing Test"))
        self.textInterface.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft PhagsPa\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.speed.setText(_translate("MainWindow", "0"))
        self.mistakes.setText(_translate("MainWindow", "0"))
        self.best_record.setText(_translate("MainWindow", "Average Stats:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
