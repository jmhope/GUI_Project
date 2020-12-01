import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

    # UI파일 연결
    # 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("LoginPage.ui")[0]
homepage = uic.loadUiType("HomePage.ui")[0]
SignUp = uic.loadUiType("SignUpPage.ui")[0]
Test_Page = uic.loadUiType("SelfTest.ui")[0]
graphpage = uic.loadUiType("GPage.ui")[0]
emissionpage = uic.loadUiType("EmissionsPage.ui")[0]


RHtml="<font color=\"red\">"#red font html tag
EFHtml="</font><br>" #end font html tag


    # 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id=None
        self.password=None
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 400, 300)
        self.setFixedSize(400, 300)

            # 버튼에 기능을 연결하는 코드
        self.lineEdit.setPlaceholderText("ID")
        self.lineEdit_2.setPlaceholderText("Password")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_2.clicked.connect(self.sign_clicked)
        self.pushButton_3.clicked.connect(self.login_clicked)


        # btn_1이 눌리면 작동할 함수
    def login_clicked(self):
        self.id = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        ##id랑 pw db에서 확인후 연
        log=HomeWindow()
        self.close()
        log.exec_()

    def sign_clicked(self):
        SU = SUWindow()
        SU.exec_()
        

class HomeWindow(QDialog, homepage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 518, 358)
        self.setFixedSize(518, 358)

        self.groupBox.setTitle("님 정보")
        #self.tab.currentTabText("기본")
        #self.groupBox.tabWidget.tab_2.tabText("등급")

        self.pushButton.clicked.connect(self.mytest)
        self.pushButton_2.clicked.connect(self.graph)
        self.pushButton_3.clicked.connect(self.emission)
        self.pushButton_4.clicked.connect(self.logout)
        self.pushButton_5.clicked.connect(self.rank)

    def mytest(self):
        TEST = TWindow()
        TEST.exec_()

    def graph(self):
        g=GW()
        g.exec_()
        print("graph")
        

    def emission(self):
        e=EW()
        e.exec_()
        print("emission") 


    def logout(self):
        self.close()

    def rank(self):
        print("rank")



class SUWindow(QDialog, SignUp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 400, 300)
        self.setFixedSize(400, 300)

        self.lineEdit.setPlaceholderText("Name")
        self.lineEdit_2.setPlaceholderText("ID")
        self.lineEdit_3.setPlaceholderText("Password")
        self.lineEdit_4.setPlaceholderText("Password")
        self.lineEdit_5.setPlaceholderText("E-Mail")
        self.lineEdit_6.setPlaceholderText("20201231 형식으로")

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancel)

    def ok(self):
        print("success")
        self.close()

    def cancel(self):
        self.close()

class TWindow(QDialog, Test_Page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 461, 311)
        self.setFixedSize(461, 311)

        #self.comboBox.addItem("교통")
        #self.comboBox.addItem("음식")
        #self.comboBox.addItem("여행")
        #self.comboBox.currentIndexChanged.connect(self.cfunction)

#    def cfunction(self):
#        self.lbl_display.setText(self.comboBox.currentText())

class GW(QDialog, graphpage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 400, 300)
        self.setFixedSize(400, 300)


class EW(QDialog, emissionpage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("C--")
        self.setGeometry(500, 300, 400, 300)
        self.setFixedSize(400, 300)
    

if __name__ == "__main__":
    main = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    main.exec_()
