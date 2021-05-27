import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QWidget, QStackedWidget, QPushButton, QGridLayout, QComboBox, \
    QLineEdit, QApplication
from collections import OrderedDict, deque
import pyqtgraph as pg
import numpy as np


class tezheng(QWidget):

    def __init__(self):
        super().__init__()
        self.class_interface()

    # welch谱估计特征
    def psd_welch_UI(self):
        self.psd_welch = QWidget()
        # self.lowpass.setFixedSize(1000, 100)
        low_layout = QGridLayout(self.psd_welch)
        lable_0 = QLabel('特征提取：', self.psd_welch)
        lable_1 = QLabel('welch谱估计', self.psd_welch)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('窗口大小：')
        lable_4 = QLabel('窗口重叠：')
        lable_5 = QLabel('采样率：')
        lable_6 = QLabel('滤波器类型：')
        self.edit1_01 = QLineEdit()
        self.edit1_02 = QLineEdit()
        self.edit1_03 = QLineEdit()
        self.comx1_01 = QComboBox()
        self.comx1_01.addItem(' ')
        self.comx1_01.addItem('巴特沃斯')
        self.comx1_01.addItem('切比雪夫1型')
        self.comx1_01.addItem('贝塞尔')
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        low_layout.addWidget(lable_0, 0, 1, 1, 2)
        low_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        low_layout.addWidget(lable_7, 1, 2, 1, 5)
        low_layout.addWidget(lable_3, 2, 2, 1, 2)
        low_layout.addWidget(self.edit1_01, 2, 4, 1, 2)
        low_layout.addWidget(lable_4, 2, 10, 1, 2)
        low_layout.addWidget(self.edit1_02, 2, 12, 1, 2)
        low_layout.addWidget(lable_5, 2, 18, 1, 2)
        low_layout.addWidget(self.edit1_03, 2, 20, 1, 2)
        low_layout.addWidget(lable_6, 3, 2, 1, 2)
        low_layout.addWidget(self.comx1_01, 3, 4, 1, 2)
        low_layout.addWidget(lable_2, 4, 5, 80, 20)
        self.psd_welch.setLayout(low_layout)

    # 复杂光谱特征
    def complex_spectrum_UI(self):
        self.complex_spectrum = QWidget()
        band_layout = QGridLayout(self.complex_spectrum)
        lable_0 = QLabel('特征提取：', self.complex_spectrum)
        lable_1 = QLabel('复杂光谱特征', self.complex_spectrum)
        lable_2 = QLabel('  ')
        lable_8 = QLabel('滤波器类型：')
        self.comx1_11 = QComboBox()
        self.comx1_11.addItem(' ')
        self.comx1_11.addItem('巴特沃斯')
        self.comx1_11.addItem('切比雪夫1型')
        self.comx1_11.addItem('贝塞尔')
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        band_layout.addWidget(lable_0, 0, 1, 1, 2)
        band_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        band_layout.addWidget(lable_7, 1, 2, 1, 5)
        band_layout.addWidget(lable_8, 3, 10, 1, 2)
        band_layout.addWidget(self.comx1_11, 3, 12, 1, 2)
        band_layout.addWidget(lable_2, 4, 5, 50, 20)
        self.complex_spectrum.setLayout(band_layout)

    # 幅度谱特征
    def magnitude_spectrum_UI(self):
        self.magnitude_spectrum = QWidget()
        band_layout = QGridLayout(self.magnitude_spectrum)
        lable_0 = QLabel('特征提取：', self.magnitude_spectrum)
        lable_1 = QLabel('幅度谱特征', self.magnitude_spectrum)
        lable_2 = QLabel('  ')
        lable_8 = QLabel('滤波器类型：')
        self.comx1_21 = QComboBox()
        self.comx1_21.addItem(' ')
        self.comx1_21.addItem('巴特沃斯')
        self.comx1_21.addItem('切比雪夫1型')
        self.comx1_21.addItem('贝塞尔')
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        band_layout.addWidget(lable_0, 0, 1, 1, 2)
        band_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        band_layout.addWidget(lable_7, 1, 2, 1, 5)
        band_layout.addWidget(lable_8, 3, 10, 1, 2)
        band_layout.addWidget(self.comx1_21, 3, 12, 1, 2)
        band_layout.addWidget(lable_2, 4, 5, 50, 20)
        self.magnitude_spectrum.setLayout(band_layout)

    # cca特征
    def cca16_UI(self, cca_index):
        self.cca16.close()
        self.cca16 = QWidget()
        self.cca_index = cca_index + 1
        cca_grid = QGridLayout()
        self.lei = ['a0', 'a1', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14',
                    'a15', 'a16']
        names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        postions = [(i, j) for i in range(2) for j in range(8)]
        for postion, name in zip(postions, names):
            if name <= self.cca_index:
                self.lei[name] = QLineEdit()
                self.lei[name].setFixedSize(80, 20)
                cca_grid.addWidget(self.lei[name], *postion)
            else:
                self.lei[name] = QLabel('   _______')
                cca_grid.addWidget(self.lei[name], *postion)
        self.cca16.setLayout(cca_grid)
        self.band_layout1.addWidget(self.cca16, 2, 2, 2, 20)

    def cca_feature_UI(self):
        self.cca16 = QWidget()
        self.cca_feature = QWidget()
        self.band_layout1 = QGridLayout()
        lable_0 = QLabel('特征提取：')
        lable_1 = QLabel('cca特征')
        lable_2 = QLabel('  ')
        lable_8 = QLabel('分类数目：')
        self.cca_comx = QComboBox()
        self.cca_comx.addItems(['', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
        self.cca_comx.currentIndexChanged[int].connect(self.cca16_UI)
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        self.band_layout1.addWidget(lable_0, 0, 1, 1, 2)
        self.band_layout1.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        self.band_layout1.addWidget(lable_7, 1, 2, 1, 5)
        self.band_layout1.addWidget(lable_8, 1, 10, 1, 2)
        self.band_layout1.addWidget(self.cca_comx, 1, 12, 1, 2)
        self.band_layout1.addWidget(lable_2, 3, 5, 40, 20)
        self.cca_feature.setLayout(self.band_layout1)

    # TRca特征

    def trca16_UI(self, trca_index):

        self.trca16.close()
        self.trca16 = QWidget()
        self.trca_index = trca_index + 1
        trca_grid = QGridLayout()
        self.lei = ['a0', 'a1', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13',
                    'a14',
                    'a15', 'a16']
        names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        postions = [(i, j) for i in range(2) for j in range(8)]
        for postion, name in zip(postions, names):
            if name <= self.trca_index:
                self.lei[name] = QLineEdit()
                self.lei[name].setFixedSize(80, 20)
                trca_grid.addWidget(self.lei[name], *postion)
            else:
                self.lei[name] = QLabel('   _______')
                trca_grid.addWidget(self.lei[name], *postion)
        self.trca16.setLayout(trca_grid)
        self.trca_layout.addWidget(self.trca16, 2, 2, 2, 20)

    def trca_feature_UI(self):
        self.trca16 = QWidget()
        self.trca_feature = QWidget()
        self.trca_layout = QGridLayout()
        lable_0 = QLabel('特征提取：')
        lable_1 = QLabel('trca特征')
        lable_2 = QLabel('  ')
        """lable_8 = QLabel('分类数目：')
        self.trca_comx = QComboBox()
        self.trca_comx.addItems(
            ['', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
        self.trca_comx.currentIndexChanged[int].connect(self.trca16_UI)"""
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        self.trca_layout.addWidget(lable_0, 0, 1, 1, 2)
        self.trca_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        self.trca_layout.addWidget(lable_7, 1, 2, 1, 5)
        # self.trca_layout.addWidget(lable_8, 1, 10, 1, 2)
        # self.trca_layout.addWidget(self.trca_comx, 1, 12, 1, 2)
        self.trca_layout.addWidget(lable_2, 3, 5, 40, 20)
        self.trca_feature.setLayout(self.trca_layout)

    # fb_cca特征
    def fbcca16_UI(self, fbcca_index):
        self.fbcca16.close()
        self.fbcca16 = QWidget()
        self.fbcca_index = fbcca_index + 1
        fbcca_grid = QGridLayout()
        self.lei2 = ['a0', 'a1', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13',
                    'a14',
                    'a15', 'a16']
        names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        postions = [(i, j) for i in range(2) for j in range(8)]
        for postion, name in zip(postions, names):
            if name <= self.fbcca_index:
                self.lei2[name] = QLineEdit()
                self.lei2[name].setFixedSize(80, 20)
                fbcca_grid.addWidget(self.lei2[name], *postion)
            else:
                self.lei2[name] = QLabel('   _______')
                fbcca_grid.addWidget(self.lei2[name], *postion)
        self.fbcca16.setLayout(fbcca_grid)
        self.band_layout2.addWidget(self.fbcca16, 2, 2, 2, 20)

    def fbcca_feature_UI(self):
        self.fbcca16 = QWidget()
        self.fbcca_feature = QWidget()
        self.band_layout2 = QGridLayout()
        lable_0 = QLabel('特征提取：')
        lable_1 = QLabel('fbcca特征')
        lable_2 = QLabel('  ')
        lable_8 = QLabel('分类数目：')
        self.fbcca_comx = QComboBox()
        self.fbcca_comx.addItems(
            ['', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
        self.fbcca_comx.currentIndexChanged[int].connect(self.fbcca16_UI)
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        self.band_layout2.addWidget(lable_0, 0, 1, 1, 2)
        self.band_layout2.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        self.band_layout2.addWidget(lable_7, 1, 2, 1, 5)
        self.band_layout2.addWidget(lable_8, 1, 10, 1, 2)
        self.band_layout2.addWidget(self.fbcca_comx, 1, 12, 1, 2)
        self.band_layout2.addWidget(lable_2, 3, 5, 40, 20)
        self.fbcca_feature.setLayout(self.band_layout2)


    def cswitch1(self, text):
        # print(text)
        if text == 'welch谱估计':
            self.stackWidget1.setCurrentIndex(0)
            self.monitor.close()
            # print(self.chass_combobox.currentIndex())
            self.monitor = monitor_feature1()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)
        if text == '复杂光谱特征':
            self.stackWidget1.setCurrentIndex(1)
            self.monitor.close()
            self.monitor = monitor_feature2()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)
        if text == '幅度谱特征':
            self.stackWidget1.setCurrentIndex(2)
            self.monitor.close()
            self.monitor = monitor_feature3()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)
        if text == 'cca特征':
            self.stackWidget1.setCurrentIndex(3)
            self.monitor.close()
            self.monitor = monitor_feature4()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)
        if text == 'trca特征':
            self.stackWidget1.setCurrentIndex(4)
            self.monitor.close()
            self.monitor = monitor_feature5()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)

        if text == 'fbcca特征':
            self.stackWidget1.setCurrentIndex(5)
            self.monitor.close()
            self.monitor = monitor_feature6()
            self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)

    def class_interface(self):
        self.chass_layout = QGridLayout()
        # self.setFixedSize(1000, 800)
        # 实例化数据流
        # self.eeg = MyThread()
        # 加载画图页面
        self.monitor = monitor_feature1()

        # 确认选择的方法
        self.chass_label = QLabel('特征提取方法:')
        self.chass_combobox = QComboBox()
        self.chass_combobox.setFixedWidth(100)
        self.chass_combobox.setFixedHeight(25)
        self.chass_combobox.addItem(' ')
        self.chass_combobox.addItem('welch谱估计')
        self.chass_combobox.addItem('复杂光谱特征')
        self.chass_combobox.addItem('幅度谱特征')
        self.chass_combobox.addItem('cca特征')
        self.chass_combobox.addItem('trca特征')
        self.chass_combobox.addItem('fbcca特征')
        # self.deal1_combobox.currentIndexChanged.connect(self.cswitch1)
        self.chass_combobox.currentIndexChanged[str].connect(self.cswitch1)

        self.chass_plot = QPushButton('显示')
        self.chass_plot.setFixedWidth(100)
        self.chass_plot.setFixedHeight(25)
        # 步骤
        # self.step_label1 = QLabel('步骤一：')
        # self.step_label2 = QLabel('步骤二：')
        # 创建参数界面
        self.psd_welch_UI()
        self.complex_spectrum_UI()
        self.magnitude_spectrum_UI()
        self.cca_feature_UI()
        self.trca_feature_UI()
        self.fbcca_feature_UI()
        # 创建stackWidget1
        self.stackWidget1 = QStackedWidget()
        # self.stackWidget1.setFixedSize(1000, 100)
        self.stackWidget1.addWidget(self.psd_welch)
        self.stackWidget1.addWidget(self.complex_spectrum)
        self.stackWidget1.addWidget(self.magnitude_spectrum)
        self.stackWidget1.addWidget(self.cca_feature)
        self.stackWidget1.addWidget(self.trca_feature)
        self.stackWidget1.addWidget(self.fbcca_feature)
        # 创建stackWidget2

        verticalLine0 = QFrame()
        verticalLine0.setFrameShape(QFrame().HLine)
        verticalLine0.setFrameShadow(QFrame().Sunken)

        verticalLine1 = QFrame()
        verticalLine1.setFrameShape(QFrame().HLine)
        verticalLine1.setFrameShadow(QFrame().Sunken)

        verticalLine2 = QFrame()
        verticalLine2.setFrameShape(QFrame().HLine)
        verticalLine2.setFrameShadow(QFrame().Sunken)

        self.chass_layout.addWidget(self.chass_label, 0, 2, 1, 10)
        self.chass_layout.addWidget(self.chass_combobox, 0, 12, 1, 10)
        self.chass_layout.addWidget(self.chass_plot, 0, 80, 1, 10)
        self.chass_layout.addWidget(verticalLine0, 1, 0, 1, 120)
        # self.deal_layout.addWidget(self.step_label1, 2, 0, 1, 10)
        self.chass_layout.addWidget(self.stackWidget1, 2, 0, 5, 120)
        self.chass_layout.addWidget(verticalLine1, 3, 0, 1, 120)
        self.chass_layout.addWidget(self.monitor, 4, 0, 20, 120)

        self.setLayout(self.chass_layout)


# 谱估计图
class monitor_feature1(QWidget):

    def __init__(self, channel_count=8, sample=65):
        QWidget.__init__(self)
        self.channel_count = channel_count
        self.sample = sample
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.create_plot1()

    def create_plot1(self):
        self.plot1 = QWidget()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='welch谱估计', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(-.5, self.channel_count + 1, padding=.01)
        self.stream_scroll_time_axis = np.linspace(0, 2 * self.sample, self.sample)
        self.stream_scroll.setXRange(0, 2 * self.sample, padding=.01)
        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '频率', 'Hz', **labelStyle)
        self.stream_scroll.setLabel('left', '通道', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(self.channel_count - 1, -1, -1):
            self.data['filtered_channel{}'.format(i + 1)] = deque([0] * self.sample)
            # print(self.filtered_data['filtered_channel{}'.format(i + 1)])
            # print(color_list[i]*255)
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in self.data['filtered_channel{}'.format(i + 1)]]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        for i in range(self.channel_count):
            current = data[i]
            current = [(point*400000 + i + 1) for point in current]
            # print('缓存区：', current)

            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                  y=([point for point in current]))


# 复杂光谱图
class monitor_feature2(QWidget):
    def __init__(self, channel_count=8, sample=258):
        QWidget.__init__(self)
        self.channel_count = channel_count
        self.sample = sample
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.curves2 = OrderedDict()
        self.create_plot2()

    def create_plot2(self):
        self.plot2 = QWidget()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='复杂光谱图', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(-.5, self.channel_count + 1, padding=.01)
        self.stream_scroll_time_axis = np.linspace(0, self.sample // 2, self.sample // 2)
        self.stream_scroll.setXRange(0, self.sample / 2, padding=.01)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '频率', 'Hz', **labelStyle)
        self.stream_scroll.setLabel('left', 'Channel', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(self.channel_count - 1, -1, -1):
            self.data['filtered_channel{}'.format(i + 1)] = deque([0] * self.sample)
            self.data['filtered_channel{}'.format(i + 1)] = np.array(self.data['filtered_channel{}'.format(i + 1)])
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in self.data['filtered_channel{}'.format(i + 1)][0:self.sample // 2]]))
            self.curves2['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[15 - i])
            self.curves2['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in
                 self.data['filtered_channel{}'.format(i + 1)][self.sample // 2:self.sample]]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        for i in range(self.channel_count):
            current = data[i]
            current = [(point*10 + i + 1) for point in current]
            # print('缓存区：', current)

            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                  y=([point for point in current[0:self.sample // 2]]))
            self.curves2['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                  y=([point for point in
                                                                      current[self.sample // 2:self.sample]]))


# 幅度谱图
class monitor_feature3(QWidget):
    def __init__(self, channel_count=8, sample=129):
        QWidget.__init__(self)
        self.channel_count = channel_count
        self.sample = sample
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.create_plot3()

    def create_plot3(self):
        self.i=0
        self.plot3 = QWidget()
        self.curves1 = OrderedDict()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='幅度谱图', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(-.5, self.channel_count + 1, padding=.01)
        self.stream_scroll_time_axis = np.linspace(0, self.sample, self.sample)
        self.stream_scroll.setXRange(0, self.sample, padding=.01)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '频率', 'Hz', **labelStyle)
        self.stream_scroll.setLabel('left', 'cca', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(self.channel_count - 1, -1, -1):
            self.data['filtered_channel{}'.format(i + 1)] = deque([0] * self.sample)
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in self.data['filtered_channel{}'.format(i + 1)]]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        self.i= self.i+1
        print('次数：', self.i)
        for i in range(self.channel_count):
            current = data[i]
            current = [(point/4 + i + 1) for point in current]
            # print('缓存区：', current)

            self.curves1['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                  y=([point for point in current]))


# cca特征图
class monitor_feature4(QWidget):
    def __init__(self, class_count=8):
        QWidget.__init__(self)
        self.class_count = class_count
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.create_plot4()

    def create_plot4(self):
        self.plot4 = QWidget()
        self.curves1 = OrderedDict()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='cca特征图', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(0, 1.2, padding=.001)
        self.stream_scroll.setXRange(0, self.class_count + 1, padding=.01)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '类', **labelStyle)
        self.stream_scroll.setLabel('left', 'cca', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(0, self.class_count, 1):
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]), y=np.array([1, 0]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        for i in range(self.class_count):
            current = data[i]
            # print('缓存区：', current)
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]),
                                                                  y=np.array([current, 0]))
# trca 特征
class monitor_feature5(QWidget):
    def __init__(self, class_count=8):
        QWidget.__init__(self)
        self.class_count = class_count
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.create_plot5()

    def create_plot5(self):
        self.plot4 = QWidget()
        self.curves1 = OrderedDict()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='trca特征图', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(0, 1.2, padding=.001)
        self.stream_scroll.setXRange(0, self.class_count + 1, padding=.01)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '类', **labelStyle)
        self.stream_scroll.setLabel('left', 'trca', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(0, self.class_count, 1):
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]), y=np.array([1, 0]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        for i in range(self.class_count):
            current = data[i]
            # print('缓存区：', current)
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]),
                                                                  y=np.array([current, 0]))

# fbcca
class monitor_feature6(QWidget):
    def __init__(self, class_count=8):
        QWidget.__init__(self)
        self.class_count = class_count
        self.data_buffer = OrderedDict()
        self.data = OrderedDict()
        self.curves1 = OrderedDict()
        self.create_plot6()

    def create_plot6(self):
        self.plot4 = QWidget()
        self.curves1 = OrderedDict()
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        # labelStyle = {'color': '#000', 'font-size': '16pt'}
        self.stream_scroll = pg.PlotWidget(title='fbca特征图', background='w')
        self.buffer_size = 1000
        self.stream_scroll.setYRange(0, 3, padding=.001)
        self.stream_scroll.setXRange(0, self.class_count + 1, padding=.01)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', '类', **labelStyle)
        self.stream_scroll.setLabel('left', 'trca', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]
        for i in range(0, self.class_count, 1):
            self.curves1['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]), y=np.array([1, 0]))
        # print(len(self.data_buffer))
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print(data)
        for i in range(self.class_count):
            current = data[i]
            # print('缓存区：', current)
            self.curves1['curve_channel{}'.format(i + 1)].setData(x=np.array([i + 1, i + 1]),
                                                                  y=np.array([current, 0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = tezheng()
    demo.show()
    sys.exit(app.exec_())