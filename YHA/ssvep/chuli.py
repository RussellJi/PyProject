from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QWidget, QStackedWidget, QPushButton, QGridLayout, QComboBox, \
     QLineEdit,QApplication
from collections import OrderedDict, deque
import pyqtgraph as pg
import numpy as np
from numpy import matlib
import sys


class dealui(QWidget):

    def __init__(self):
        super().__init__()
        self.deal_interface()

    # 低通滤波
    def lowpass_UI(self):
        self.lowpass = QWidget()
        # self.lowpass.setFixedSize(1000, 100)
        low_layout = QGridLayout(self.lowpass)
        lable_0 = QLabel('步骤一：', self.lowpass)
        lable_1 = QLabel('低通滤波', self.lowpass)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('采样率：')
        lable_4 = QLabel('截止频率：')
        lable_5 = QLabel('阶数：')
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
        low_layout.addWidget(lable_2, 4, 5, 50, 20)

        self.lowpass.setLayout(low_layout)

    # 带通滤波器
    def bandpass_UI(self):
        self.bandpass = QWidget()
        band_layout = QGridLayout(self.bandpass)
        lable_0 = QLabel('步骤一：', self.bandpass)
        lable_1 = QLabel('带通滤波', self.bandpass)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('采样率：')
        lable_4 = QLabel('中心频率：')
        lable_5 = QLabel('带宽：')
        lable_6 = QLabel('阶数：')
        lable_8 = QLabel('滤波器类型：')
        self.edit1_11 = QLineEdit()
        self.edit1_12 = QLineEdit()
        self.edit1_13 = QLineEdit()
        self.edit1_14 = QLineEdit()
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
        band_layout.addWidget(lable_3, 2, 2, 1, 2)
        band_layout.addWidget(self.edit1_11, 2, 4, 1, 2)
        band_layout.addWidget(lable_4, 2, 10, 1, 2)
        band_layout.addWidget(self.edit1_12, 2, 12, 1, 2)
        band_layout.addWidget(lable_5, 2, 18, 1, 2)
        band_layout.addWidget(self.edit1_13, 2, 20, 1, 2)
        band_layout.addWidget(lable_6, 3, 2, 1, 2)
        band_layout.addWidget(self.edit1_14, 3, 4, 1, 2)
        band_layout.addWidget(lable_8, 3, 10, 1, 2)
        band_layout.addWidget(self.comx1_11, 3, 12, 1, 2)
        band_layout.addWidget(lable_2, 4, 5, 50, 20)
        self.bandpass.setLayout(band_layout)

    # 高通滤波器
    def highpass_UI(self):
        self.highpass = QWidget()
        high_layout = QGridLayout(self.highpass)
        lable_0 = QLabel('步骤一：', self.highpass)
        lable_1 = QLabel('高通滤波', self.highpass)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('采样率：')
        lable_4 = QLabel('截止频率：')
        lable_5 = QLabel('阶数：')
        lable_6 = QLabel('滤波器类型：')
        self.edit1_21 = QLineEdit()
        self.edit1_22 = QLineEdit()
        self.edit1_23 = QLineEdit()
        self.comx1_21 = QComboBox()
        self.comx1_21.addItem(' ')
        self.comx1_21.addItem('巴特沃斯')
        self.comx1_21.addItem('切比雪夫1型')
        self.comx1_21.addItem('贝塞尔')
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        high_layout.addWidget(lable_0, 0, 1, 1, 2)
        high_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        high_layout.addWidget(lable_7, 1, 2, 1, 5)
        high_layout.addWidget(lable_3, 2, 2, 1, 2)
        high_layout.addWidget(self.edit1_21, 2, 4, 1, 2)
        high_layout.addWidget(lable_4, 2, 10, 1, 2)
        high_layout.addWidget(self.edit1_22, 2, 12, 1, 2)
        high_layout.addWidget(lable_5, 2, 18, 1, 2)
        high_layout.addWidget(self.edit1_23, 2, 20, 1, 2)
        high_layout.addWidget(lable_6, 3, 2, 1, 2)
        high_layout.addWidget(self.comx1_21, 3, 4, 1, 2)
        high_layout.addWidget(lable_2, 4, 5, 50, 20)

        self.highpass.setLayout(high_layout)

    # 滤波
    def Trca_UI(self):
        self.trca = QWidget()
        lable6 = QLabel('带通滤波', self.trca)
        lable6.setFont(QFont("Microsoft YaHei", 50, 100))
        lable6.move(300, 20)

    # 小波变换
    def wavelet_filter_UI(self):
        self.wavelet_filter = QWidget()
        wavelet_layout = QGridLayout(self.wavelet_filter)
        lable_0 = QLabel('步骤二：', self.wavelet_filter)
        lable_1 = QLabel('小波变换', self.wavelet_filter)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('小波基：')
        lable_4 = QLabel('分解级数：')
        self.edit2_01 = QLineEdit()
        self.edit2_02 = QLineEdit()
        lable_6 = QLabel(' ')
        lable_8 = QLabel("小波基可选内容：db1..db15，haar，sym2..sym10，coif1..coif5，bior1.1，bior1.3，bior1.5，bior2.2，"
                         "bior2.4，bior2.6，bior2 .8，bior3.1，")
        lable_9 = QLabel("bior3.3，bior3.5，bior3.7，bior3.9，bior4.4，bior5.5，bior6.8")
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        wavelet_layout.addWidget(lable_0, 0, 1, 1, 2)
        wavelet_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        wavelet_layout.addWidget(lable_7, 1, 2, 1, 5)
        wavelet_layout.addWidget(lable_3, 2, 2, 1, 2)
        wavelet_layout.addWidget(self.edit2_02, 2, 4, 1, 3)
        wavelet_layout.addWidget(lable_4, 2, 11, 1, 2)
        wavelet_layout.addWidget(self.edit2_01, 2, 13, 1, 2)
        wavelet_layout.addWidget(lable_6, 3, 1, 1, 10)
        wavelet_layout.addWidget(lable_8, 4, 2, 1, 25)
        wavelet_layout.addWidget(lable_9, 5, 2, 1, 25)
        wavelet_layout.addWidget(lable_2, 6, 5, 50, 20)

        self.wavelet_filter.setLayout(wavelet_layout)

    # 平滑滤波
    def rolling_filter_UI(self):
        self.rolling_filter = QWidget()
        rolling_layout = QGridLayout(self.rolling_filter)
        lable_0 = QLabel('步骤二：', self.rolling_filter)
        lable_1 = QLabel('平滑滤波', self.rolling_filter)
        lable_2 = QLabel('  ')
        lable_3 = QLabel('窗口大小：')
        lable_4 = QLabel('操纵模式：')
        self.edit2_11 = QLineEdit()
        self.comx2_11 = QComboBox()
        self.comx2_11.setFixedWidth(120)
        self.comx2_11.setFixedHeight(20)
        self.comx2_11.addItem(' ')
        self.comx2_11.addItem('平均数')
        self.comx2_11.addItem('中位数')
        lable_7 = QLabel('  ')
        # lable_5 = QLabel(' ')
        rolling_layout.addWidget(lable_0, 0, 1, 1, 2)
        rolling_layout.addWidget(lable_1, 0, 3, 1, 2)
        # low_layout.addWidget(lable_5, 0, 3, 1, 10)
        rolling_layout.addWidget(lable_7, 1, 2, 1, 5)
        rolling_layout.addWidget(lable_3, 2, 2, 1, 2)
        rolling_layout.addWidget(self.edit2_11, 2, 4, 1, 2)
        rolling_layout.addWidget(lable_4, 2, 9, 1, 2)
        rolling_layout.addWidget(self.comx2_11, 2, 11, 1, 2)
        rolling_layout.addWidget(lable_2, 4, 5, 50, 20)
        self.rolling_filter.setLayout(rolling_layout)

    def pca_filter_UI(self):
        self.pca_filter = QWidget()
        lable6 = QLabel('PCA', self.pca_filter)
        lable6.setFont(QFont("Microsoft YaHei", 50, 100))
        lable6.move(420, 20)

    def ica_filter_UI(self):
        self.ica_filter = QWidget()
        lable7 = QLabel('ICA', self.ica_filter)
        lable7.setFont(QFont("Microsoft YaHei", 50, 100))
        lable7.move(420, 20)

    def kong_UI(self):
        self.kong_filter = QWidget()
        lable7 = QLabel('无', self.kong_filter)
        lable7.setFont(QFont("Microsoft YaHei", 50, 100))
        lable7.move(500, 20)

    def cswitch1(self, text):
        # print(text)
        if text == '低通':
            self.stackWidget1.setCurrentIndex(0)
        if text == '带通':
            self.stackWidget1.setCurrentIndex(1)
        if text == '高通':
            self.stackWidget1.setCurrentIndex(2)
        if text == '带通滤波':
            self.stackWidget1.setCurrentIndex(3)

    def cswitch2(self, text):
        if text == '小波变换':
            self.stackWidget2.setCurrentIndex(0)
        if text == '平滑滤波':
            self.stackWidget2.setCurrentIndex(1)
        if text == 'PCA':
            self.stackWidget2.setCurrentIndex(2)
        if text == 'ICA':
            self.stackWidget2.setCurrentIndex(3)
        if text == '空':
            self.stackWidget2.setCurrentIndex(4)

    def deal_interface(self):
        self.deal_layout = QGridLayout()
        # self.setFixedSize(1000, 800)
        # 实例化数据流
        # self.eeg = MyThread()
        self.deal_label = QLabel('预处理方法:')
        self.deal1_combobox = QComboBox()
        self.deal1_combobox.setFixedWidth(100)
        self.deal1_combobox.setFixedHeight(25)
        self.deal1_combobox.addItem(' ')
        self.deal1_combobox.addItem('低通')
        self.deal1_combobox.addItem('带通')
        self.deal1_combobox.addItem('高通')
        self.deal1_combobox.addItem('带通滤波')
        # self.deal1_combobox.currentIndexChanged.connect(self.cswitch1)
        self.deal1_combobox.currentIndexChanged[str].connect(self.cswitch1)

        self.deal2_combobox = QComboBox()
        self.deal2_combobox.setFixedWidth(100)
        self.deal2_combobox.setFixedHeight(25)
        self.deal2_combobox.addItem(' ')
        self.deal2_combobox.addItem('小波变换')
        self.deal2_combobox.addItem('平滑滤波')
        self.deal2_combobox.addItem('PCA')
        self.deal2_combobox.addItem('ICA')
        self.deal2_combobox.addItem('空')
        self.deal_plot = QPushButton('显示')
        self.deal_plot.setFixedWidth(100)
        self.deal_plot.setFixedHeight(25)
        self.deal2_combobox.currentIndexChanged[str].connect(self.cswitch2)
        # 步骤
        # self.step_label1 = QLabel('步骤一：')
        # self.step_label2 = QLabel('步骤二：')
        # 创建参数界面
        self.lowpass_UI()
        self.bandpass_UI()
        self.highpass_UI()
        self.Trca_UI()
        self.wavelet_filter_UI()
        self.rolling_filter_UI()
        self.pca_filter_UI()
        self.ica_filter_UI()
        self.kong_UI()
        # 创建stackWidget1
        self.stackWidget1 = QStackedWidget()
        # self.stackWidget1.setFixedSize(1000, 100)
        self.stackWidget1.addWidget(self.lowpass)
        self.stackWidget1.addWidget(self.bandpass)
        self.stackWidget1.addWidget(self.highpass)
        self.stackWidget1.addWidget(self.trca)
        # 创建stackWidget2
        self.stackWidget2 = QStackedWidget()
        # self.stackWidget2.setFixedSize(1000, 100)
        self.stackWidget2.addWidget(self.wavelet_filter)
        self.stackWidget2.addWidget(self.rolling_filter)
        self.stackWidget2.addWidget(self.pca_filter)
        self.stackWidget2.addWidget(self.ica_filter)
        self.stackWidget2.addWidget(self.kong_filter)

        verticalLine0 = QFrame()
        verticalLine0.setFrameShape(QFrame().HLine)
        verticalLine0.setFrameShadow(QFrame().Sunken)

        verticalLine1 = QFrame()
        verticalLine1.setFrameShape(QFrame().HLine)
        verticalLine1.setFrameShadow(QFrame().Sunken)

        verticalLine2 = QFrame()
        verticalLine2.setFrameShape(QFrame().HLine)
        verticalLine2.setFrameShadow(QFrame().Sunken)

        self.monitor = Monitor_Widget()
        # self.monitor.setFixedSize(950, 600)

        self.deal_layout.addWidget(self.deal_label, 0, 2, 1, 10)
        self.deal_layout.addWidget(self.deal1_combobox, 0, 12, 1, 10)
        self.deal_layout.addWidget(self.deal2_combobox, 0, 27, 1, 10)
        self.deal_layout.addWidget(self.deal_plot, 0, 80, 1, 10)
        self.deal_layout.addWidget(verticalLine0, 1, 0, 1, 120)
        # self.deal_layout.addWidget(self.step_label1, 2, 0, 1, 10)
        self.deal_layout.addWidget(self.stackWidget1, 2, 0, 5, 120)
        self.deal_layout.addWidget(verticalLine1, 3, 0, 1, 120)
        # self.deal_layout.addWidget(self.step_label2, 5, 0, 1, 10)
        self.deal_layout.addWidget(self.stackWidget2, 4, 0, 5, 120)
        self.deal_layout.addWidget(verticalLine2, 5, 0, 1, 120)
        self.deal_layout.addWidget(self.monitor, 6, 0, 20, 120)

        self.setLayout(self.deal_layout)


# 脑电显示界面
class Monitor_Widget(QWidget):

    def __init__(self, chaannel_count=8, samples=256):
        QWidget.__init__(self)
        self.channel_count = chaannel_count
        self.samples = samples
        self.curves = OrderedDict()
        self.data_buffer = OrderedDict()
        self.filtered_data = OrderedDict()
        self.create_plot()

    def create_plot(self):
        # 数据的流动
        self.t = 0
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.stream_scroll = pg.PlotWidget(title='脑电图', background='w')
        self.stream_scroll.setYRange(0.5, self.channel_count, padding=0.1)

        self.stream_scroll_time_axis = np.linspace(-5, 0, self.samples * 4)
        self.stream_scroll.setXRange(-5, 0, padding=.005)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', 'Time', 'Seconds', **labelStyle)
        self.stream_scroll.setLabel('left', 'Channel', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]

        for i in range(self.channel_count - 1, -1, -1):
            self.filtered_data['filtered_channel{}'.format(i + 1)] = matlib.repmat([0], self.samples * 4, 1).T.ravel()
            self.curves['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in self.filtered_data['filtered_channel{}'.format(i + 1)]]))
        # print(len(self.data_buffer))
        self.set_layout()

    def set_layout(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        self.t=self.t+1
        print("num", self.t)
        self.current = []
        for i in range(self.channel_count):
            current1 = data[i]
            self.filtered_data['filtered_channel{}'.format(i + 1)] \
                = np.append(self.filtered_data['filtered_channel{}'.format(i + 1)][self.samples:], current1)
            self.current = self.filtered_data['filtered_channel{}'.format(i + 1)]
            current = [(point/3000 + i + 1) for point in self.current]
            self.curves['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                 y=([point for point in current]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dealui()
    ex.show()
    sys.exit(app.exec_())