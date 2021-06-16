import os
import sys
from socket import *
import time
import gzip
import pickle
import numpy as np

from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMutex
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow, QFrame, \
    QSplitter, QStackedWidget, QDockWidget, QListWidget
from data_eeg import MyThread
from boardz import board1, Stream_Monitor_Widget
from chuli import dealui, Monitor_Widget
from tezhengtiqu import tezheng, monitor_feature1, monitor_feature2, monitor_feature3, monitor_feature4, monitor_feature5,monitor_feature6
from model_GUI import model
from game_GUI import game

a = "m"

class Thread_3(QThread):

    def __init__(self):
        super().__init__()

    def run(self):

        print("nb")

        # 小车

        address = ('192.168.4.1', 8888)  # 服务端地址和端口
        s = socket(AF_INET, SOCK_STREAM)
        try:
            print("dodo")
            s.connect(address)  # 尝试连接服务端
        except Exception:
            print('[!] Server not found ot not open')
            sys.exit()
        while True:
            time.sleep(1)
            print("传输：",a)
            s.sendall(a.encode())
            if a == 'q':  # 自定义结束字符串
                break
        s.close()


class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.jiemian()

    def boardUI(self):
        self.board = board1()

    def b_xianshi(self):
        # print('wewewef')
        try:
            self.num_channel = int(self.board.edit_b1.text())
            # print(num_channel)
            self.num_sample = int(self.board.edit_b2.text())
            self.board.monitor.close()
            self.board.monitor = Stream_Monitor_Widget(self.num_channel, self.num_sample)
            self.board.board_layout.addWidget(self.board.monitor, 6, 0, 10, 40)
        except Exception:
            print('请输入板子参数')

        try:
            self.data.org_signal.connect(self.board.monitor.update_plot)
            self.data.puanduan1 = True
        except Exception:
            print('请连接板子')

    def p_xianshi(self):
        # print('wewewef')
        self.num_channel = int(self.board.edit_b1.text())
        # print(num_channel) 
        self.num_sample = int(self.board.edit_b2.text())
        self.deal.monitor.close()
        self.deal.monitor = Monitor_Widget(self.num_channel, self.num_sample)
        self.deal.deal_layout.addWidget(self.deal.monitor, 6, 0, 20, 120)
        self.data.pre_signal.connect(self.deal.monitor.update_plot)
        self.data.puanduan2 = True

    def f_xianshi(self):
        self.num_channel = int(self.board.edit_b1.text())
        # print(num_channel)
        self.num_sample = int(self.board.edit_b2.text())
        self.characteristic.monitor.close()
        if self.characteristic.chass_combobox.currentIndex() == 1:
            self.characteristic.monitor = monitor_feature1(self.num_channel, int(int(self.characteristic.edit1_01.text())/2+1))
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        elif self.characteristic.chass_combobox.currentIndex() == 2:
            print(2*(self.num_sample/2+1))
            self.characteristic.monitor = monitor_feature2(self.num_channel, int(2*(self.num_sample/2+1)))
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        elif self.characteristic.chass_combobox.currentIndex() == 3:
            self.characteristic.monitor = monitor_feature3(self.num_channel, int(self.num_sample/2+1))
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        elif self.characteristic.chass_combobox.currentIndex() == 4:
            self.characteristic.monitor = monitor_feature4(self.characteristic.cca_index)
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        elif self.characteristic.chass_combobox.currentIndex() == 5:
            self.characteristic.monitor = monitor_feature5(8)
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        elif self.characteristic.chass_combobox.currentIndex() == 6:
            self.characteristic.monitor = monitor_feature6(self.characteristic.fbcca_index)
            self.characteristic.chass_layout.addWidget(self.characteristic.monitor, 4, 0, 20, 120)
            self.data.feature_signal.connect(self.characteristic.monitor.update_plot)
        self.data.puanduan3 = True
    # def connect():
        self.data.command_signal.connect(self.bianhua)


    def bianhua(self,i):
        global a

        if i == "1":
            a = "1"
            time.sleep(1)
            a = "k"
        elif i == "2":
            a = "2"
            time.sleep(1)
            a = "k"
        elif i =="3":
            a = "3"
            time.sleep(1)
            a = "k"
        elif i =="4":
            a="5"
            time.sleep(1)
            a = "k"
        elif i =="5":
            a="9"
            time.sleep(1)
            a = "k"
        elif i =="6":
            a="8"
            time.sleep(1)
            a = "k"
        elif i =="7":
            a="7"
            time.sleep(1)
            a = "k"
        elif i =="8":
            a="4"
            time.sleep(1)
            a = "k"
        print(a)



    def dealUI(self):
        self.deal = dealui()

    def characteristicUI(self):
        self.characteristic = tezheng()

    def modelUI(self):
        self.class_model = model()

    def gameUI(self):
        self.application = game()

    def stackSwitch(self, index):
        self.stackWidget.setCurrentIndex(index)

    def jiemian(self):

        # 实例化线程对象
        # self.data = MyThread()
        # 线程自定义信号连接的槽函数

        self.test_window1 = QMainWindow()
        self.setWindowTitle("测试平台")
        self.setWindowIcon(QIcon('E:/学习/test_platform/Hardware_software_testing/png/脑机接口.jpg'))
        self.command = QWidget()

        # 加载页面
        self.boardUI()
        self.dealUI()
        self.characteristicUI()
        self.modelUI()
        self.gameUI()
        # 设置显示原始数据按钮
        self.board.dispay.clicked.connect(self.b_xianshi)
        # 设置显示预处理数据按钮
        self.deal.deal_plot.clicked.connect(self.p_xianshi)
        # 设置显示特征数据显示
        self.characteristic.chass_plot.clicked.connect(self.f_xianshi)
        # 创建表各界面和QDockWidget界面
        # 将列表放到QDockWidget界面中
        self.listwidget = QListWidget()
        self.listwidget.setFixedSize(100, 600)
        self.listwidget.addItem('脑电放大器')
        self.listwidget.addItem('脑电预处理')
        self.listwidget.addItem('脑电特征提取')
        self.listwidget.addItem('脑电分类模型')
        self.listwidget.addItem('脑控游戏')
        font = QFont()
        font.setFamily("Microsoft YaHei")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(11)  # 括号里的数字可以设置成自己想要的字体大小
        self.listwidget.setFont(font)
        self.items = QDockWidget()
        self.items.setWidget(self.listwidget)
        self.test_window1.addDockWidget(Qt.LeftDockWidgetArea, self.items)

        # 创建QStackedWidget窗口
        self.stackWidget = QStackedWidget()
        self.stackWidget.addWidget(self.board)
        self.stackWidget.addWidget(self.deal)
        self.stackWidget.addWidget(self.characteristic)
        self.stackWidget.addWidget(self.class_model)
        self.stackWidget.addWidget(self.application)
        self.test_window1.setCentralWidget(self.stackWidget)
        self.listwidget.currentRowChanged.connect(self.stackSwitch)

        """
        窗口2
        """
        self.test_window2 = QFrame()
        self.test_window2.setFrameShape(QFrame.Box)
        self.test_window2.setFrameShadow(QFrame.Sunken)
        self.test_window2.setLineWidth(2)
        self.labe2 = QLabel('结果', self.test_window2)
        self.button = QPushButton('开始', self.test_window2)
        self.button.clicked.connect(self.count_func)
        self.button_2 = QPushButton('停止', self.test_window2)
        self.button_2.clicked.connect(self.stop_count_func)
        self.button_3 = QPushButton('传输命令', self.test_window2)
        self.button_3.clicked.connect(self.contral)



        self.h_box = QHBoxLayout()
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.button)
        self.h_box.addWidget(self.button_2)
        self.h_box.addWidget(self.button_3)


        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.labe2)
        self.v_box.addStretch(1)
        self.v_box.addLayout(self.h_box)
        self.test_window2.setLayout(self.v_box)


        self.splitter = QSplitter()
        self.splitter.addWidget(self.test_window1)

        self.splitter.addWidget(self.test_window2)
        self.splitter.setOrientation(Qt.Vertical)
        self.setCentralWidget(self.splitter)

    def contral(self):
        self.thread_3 = Thread_3()
        self.thread_3.start()


    def stop_count_func(self):

        self.data.is_on = False

    def count_func(self):
        # 获取板子参数
        board_set = [self.board.boardComboxBox.currentIndex() - 2, self.board.edit_b4.text(),
                     int(self.board.edit_b1.text()),
                     int(self.board.edit_b2.text()), float(self.board.edit_b3.text())]
        # 获取预处理参数
        pre_set1 = []
        pre_set2 = []
        # 设置预处理1的列表
        if self.deal.deal1_combobox.currentIndex() == 1:
            pre_set1.append(0)
            pre_set1.append(int(self.deal.edit1_01.text()))
            pre_set1.append(int(self.deal.edit1_02.text()))
            pre_set1.append(int(self.deal.edit1_03.text()))
            pre_set1.append(self.deal.comx1_01.currentIndex() - 1)
            pre_set1.append(int(self.board.edit_b1.text()))
        elif self.deal.deal1_combobox.currentIndex() == 2:
            pre_set1.append(1)
            pre_set1.append(int(self.deal.edit1_11.text()))
            pre_set1.append(int(self.deal.edit1_12.text()))
            pre_set1.append(int(self.deal.edit1_13.text()))
            pre_set1.append(int(self.deal.edit1_14.text()))
            pre_set1.append(self.deal.comx1_11.currentIndex() - 1)
            pre_set1.append(int(self.board.edit_b1.text()))
        elif self.deal.deal1_combobox.currentIndex() == 3:
            pre_set1.append(2)
            pre_set1.append(int(self.deal.edit1_21.text()))
            pre_set1.append(int(self.deal.edit1_22.text()))
            pre_set1.append(int(self.deal.edit1_23.text()))
            pre_set1.append(self.deal.comx1_21.currentIndex() - 1)
            pre_set1.append(int(self.board.edit_b1.text()))
        elif self.deal.deal1_combobox.currentIndex() == 4:
            pre_set1.append(3)
            pre_set1.append(int(self.board.edit_b2.text()))
            pre_set1.append(float(self.board.edit_b3.text()))

        # 设置预处理2列表
        if self.deal.deal2_combobox.currentIndex() == 1:
            pre_set2.append(0)
            pre_set2.append(self.deal.edit2_02.text())
            pre_set2.append(int(self.deal.edit2_01.text()))
            pre_set2.append(int(self.board.edit_b1.text()))
        elif self.deal.deal2_combobox.currentIndex() == 2:
            pre_set2.append(1)
            pre_set2.append(int(self.deal.edit2_11.text()))
            pre_set2.append(self.deal.comx2_11.currentIndex() - 1)
            pre_set2.append(int(self.board.edit_b1.text()))
        elif self.deal.deal2_combobox.currentIndex() == 3:
            pre_set2.append(2)
            pre_set2.append(int(self.board.edit_b1.text()))
        elif self.deal.deal2_combobox.currentIndex() == 4:
            pre_set2.append(3)
            pre_set2.append(int(self.board.edit_b1.text()))
        elif self.deal.deal2_combobox.currentIndex() == 5:
            pre_set2.append(4)

        pre_set = [pre_set1, pre_set2]
        # 获取特征提取列表
        chass_list = []
        if self.characteristic.chass_combobox.currentIndex() == 1:
            chass_list.append(0)
            chass_list.append(int(self.characteristic.edit1_01.text()))
            chass_list.append(int(self.characteristic.edit1_02.text()))
            chass_list.append(int(self.characteristic.edit1_03.text()))
            chass_list.append(self.characteristic.comx1_01.currentIndex()-1)
            chass_list.append(int(self.board.edit_b1.text()))
        elif self.characteristic.chass_combobox.currentIndex() == 2:
            chass_list.append(1)
            chass_list.append(self.characteristic.comx1_11.currentIndex()-1)
            chass_list.append(int(self.board.edit_b1.text()))
        elif self.characteristic.chass_combobox.currentIndex() == 3:
            chass_list.append(2)
            chass_list.append(self.characteristic.comx1_21.currentIndex() - 1)
            chass_list.append(int(self.board.edit_b1.text()))
        elif self.characteristic.chass_combobox.currentIndex() == 4:
            chass = []
            chass_list.append(3)
            for i in range(1, self.characteristic.cca_index + 1, 1):
                chass.append(float(self.characteristic.lei[i].text()))
            chass_list.append(chass)
            chass_list.append(int(self.board.edit_b2.text()))
            chass_list.append(float(self.board.edit_b3.text()))
            chass_list.append(self.characteristic.cca_index)
        elif self.characteristic.chass_combobox.currentIndex() == 5:
            chass_list.append(4)
            chass_list.append(8)
        elif self.characteristic.chass_combobox.currentIndex() == 6:
            chass = []
            chass_list.append(5)
            for i in range(1, self.characteristic.fbcca_index+1, 1):
                chass.append(float(self.characteristic.lei2[i].text()))
            chass_list.append(chass)
            chass_list.append(int(self.board.edit_b2.text()))
            chass_list.append(float(self.board.edit_b3.text()))
            chass_list.append(self.characteristic.fbcca_index)
            print("列表：",chass_list)

        # 实例化数据获取
        self.data = MyThread(board_set, pre_set, chass_list)
        self.data.is_on = True
        self.data.start()  # 启动线程


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
