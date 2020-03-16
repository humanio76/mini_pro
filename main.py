import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5 import uic
from lib.YouViewLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from PyQt5 import QtWebEngineWidgets
import re
import datetime


#from_class=uic.loadUiType('D:/mini_pro/ui/basic_mhp.ui')[0]

class Main(QMainWindow, Ui_MainWindow): #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자 호출
        #초기화
        self.setupUi(self) # 함수 선언
        #인증버튼 이벤트 전
        self.initAuthLock()
        #setupUI
        #인증버튼 이벤트 후
        self.initAuthUnlock()

        #시그널 초기화
        self.initSignal()

        #로그인 관련 변수 선언(로그인 정보를 담을 변수)
        self.user_id=None
        self.user_pw=None



    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')


    def initAuthUnlock(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)

    @pyqtSlot() #명시적 표현(유지보수 때문에 슬롯과 시그널이 여러개일 때 시그널은 시그널끼리 슬롯은 슬롯끼리 모아 놓는 책깔피 개념)
    def authCheck(self):
        #print('test')
        dlg=AuthDialog()
        dlg.exec_()
        self.user_id=dlg.user_id
        self.user_pw=dlg.user_pw
        #print("id : %s Password : %s" %(self.user_id,self.user_pw))
        #이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용자 유효기간을 체크하는 코딩

        if True: #강제로 아이디 비번 모두 인증완료
            self.initAuthUnlock()#로그인후 모두 비활성화
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False) #로그인버튼 비활성화
            self.urlTextEdit.setFocus(True) #커서이동
        else:
            QMessageBox.about(self, "인증오류","아이디 또는 비밀번호가 맞지 않습니다.")






if __name__ == "__main__":     # 클래스 전체 호출
    app=QApplication(sys.argv)
    you_viewer_main=Main()
    you_viewer_main.show()
    app.exec_()
