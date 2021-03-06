# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_mhp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 729)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/mini_pro/resource/coffee-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 211, 401))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/mini_pro/resource/mhpark_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(50, 140, 101, 41))
        self.loginButton.setObjectName("loginButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(2, 200, 201, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 0, 591, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webEngineView.setGeometry(QtCore.QRect(10, 20, 571, 371))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 410, 811, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 391, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 39, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(21, 87, 56, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(25, 139, 56, 12))
        self.label_4.setObjectName("label_4")
        self.previewButton = QtWidgets.QPushButton(self.groupBox_3)
        self.previewButton.setGeometry(QtCore.QRect(330, 31, 51, 31))
        self.previewButton.setObjectName("previewButton")
        self.streamComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.streamComboBox.setGeometry(QtCore.QRect(80, 130, 301, 31))
        self.streamComboBox.setObjectName("streamComboBox")
        self.startButton = QtWidgets.QPushButton(self.groupBox_3)
        self.startButton.setGeometry(QtCore.QRect(227, 170, 75, 41))
        self.startButton.setObjectName("startButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox_3)
        self.exitButton.setGeometry(QtCore.QRect(307, 170, 75, 41))
        self.exitButton.setObjectName("exitButton")
        self.fileNavButton = QtWidgets.QToolButton(self.groupBox_3)
        self.fileNavButton.setGeometry(QtCore.QRect(330, 80, 51, 31))
        self.fileNavButton.setObjectName("fileNavButton")
        self.pathTextEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.pathTextEdit.setReadOnly(True)
        self.pathTextEdit.setGeometry(QtCore.QRect(80, 80, 241, 31))
        self.pathTextEdit.setObjectName("pathTextEdit")
        self.urlTextEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.urlTextEdit.setGeometry(QtCore.QRect(80, 30, 241, 31))
        self.urlTextEdit.setObjectName("urlTextEdit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 430, 401, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setGeometry(QtCore.QRect(-17, 0, 20, 291))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 381, 191))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(399, 420, 20, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 680, 81, 16))
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(90, 677, 20, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.loadProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.loadProgress.setGeometry(QtCore.QRect(107, 676, 291, 23))
        self.loadProgress.setProperty("value", 0)
        self.loadProgress.setObjectName("loadProgress")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 680, 81, 16))
        self.label_6.setObjectName("label_6")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(509, 675, 311, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(490, 677, 20, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "기본정보"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.groupBox_2.setTitle(_translate("MainWindow", "player"))
        self.groupBox_3.setTitle(_translate("MainWindow", "다운로드 URL 저장 위치"))
        self.label_2.setText(_translate("MainWindow", "Video URL :"))
        self.label_3.setText(_translate("MainWindow", "save To :"))
        self.label_4.setText(_translate("MainWindow", "Stream :"))
        self.previewButton.setText(_translate("MainWindow", "확인"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.exitButton.setText(_translate("MainWindow", "END"))
        self.fileNavButton.setText(_translate("MainWindow", "..."))
        self.groupBox_4.setTitle(_translate("MainWindow", "log"))
        self.label_5.setText(_translate("MainWindow", "브라우저 로딩"))
        self.label_6.setText(_translate("MainWindow", "브라우저 로딩"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
