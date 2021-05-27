import sys
from collections import OrderedDict, deque
from sklearn import preprocessing
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QComboBox, QStackedWidget, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QVBoxLayout, QApplication, QFrame
import pyqtgraph as pg
import numpy as np
# from get_eeg import Get_eeg
from numpy import matlib


class board1(QWidget):

    def __init__(self):
        super().__init__()
        self.board_interface()


    def board_interface(self):
        # 第一层
        self.board_layout = QGridLayout()
        boardlabel = QLabel('脑电放大器')
        boardlabel.setFont(QFont("Microsoft YaHei", 20, 50))
        label_1 = QLabel('通道数：')
        label_2 = QLabel('采样点数：')
        label_3 = QLabel('步长：')
        label_4 = QLabel('板子选择：')
        label_5 = QLabel('端口号：')
        self.edit_b1 = QLineEdit()
        self.edit_b1.setFixedSize(100, 20)
        self.edit_b2 = QLineEdit()
        self.edit_b2.setFixedSize(100, 20)
        self.edit_b3 = QLineEdit()
        self.edit_b3.setFixedSize(100, 20)
        self.edit_b4 = QLineEdit()
        self.edit_b4.setFixedSize(120, 20)
        self.boardComboxBox = QComboBox()
        self.boardComboxBox.addItem('')
        self.boardComboxBox.addItem('模拟数据')
        self.boardComboxBox.addItem('cyton_board')
        self.boardComboxBox.addItem('cyton_daisy_board')
        self.boardComboxBox.addItem('cyton_wifi_board')
        self.boardComboxBox.addItem('cyton_daisy_wifi_board')
        self.boardComboxBox.setFixedWidth(100)
        self.boardComboxBox.setFixedHeight(20)

        self.dispay = QPushButton('显示')
        self.dispay.setFixedSize(80, 20)

        verticalLine0 = QFrame()
        verticalLine0.setFrameShape(QFrame().HLine)
        verticalLine0.setFrameShadow(QFrame().Sunken)

        verticalLine1 = QFrame()
        verticalLine1.setFrameShape(QFrame().HLine)
        verticalLine1.setFrameShadow(QFrame().Sunken)

        self.monitor = Stream_Monitor_Widget()

        self.board_layout.addWidget(boardlabel, 0, 17, 1, 2)
        self.board_layout.addWidget(verticalLine0, 1, 0, 1, 40)
        self.board_layout.addWidget(label_4, 3, 6, 1, 1)
        self.board_layout.addWidget(self.boardComboxBox, 3, 7, 1, 1)
        self.board_layout.addWidget(label_5, 3, 13, 1, 1)
        self.board_layout.addWidget(self.edit_b4, 3, 14, 1, 2)
        self.board_layout.addWidget(label_1, 3, 17, 1, 1)
        self.board_layout.addWidget(self.edit_b1, 3, 18, 1, 1)
        self.board_layout.addWidget(label_2, 3, 20, 1, 1)
        self.board_layout.addWidget(self.edit_b2, 3, 21, 1, 1)
        self.board_layout.addWidget(label_3, 3, 23, 1, 1)
        self.board_layout.addWidget(self.edit_b3, 3, 24, 1, 2)
        self.board_layout.addWidget(self.dispay, 3, 29)
        self.board_layout.addWidget(verticalLine1, 5, 0, 1, 40)
        self.board_layout.addWidget(self.monitor, 6, 0, 10, 40)

        self.setLayout(self.board_layout)


class Stream_Monitor_Widget(QWidget):

    def __init__(self, chaannel_count=8, samples=256):
        QWidget.__init__(self)
        self.min_max_scaler = preprocessing.MinMaxScaler(feature_range=[-0.5, 0.5])
        self.channel_count = chaannel_count
        self.samples = samples
        self.curves = OrderedDict()
        self.data_buffer = OrderedDict()
        self.filtered_data = np.zeros((chaannel_count,samples*3))
        self.create_plot()

    def create_plot(self):
        # 数据的流动
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.stream_scroll = pg.PlotWidget(title='脑电图', background='w')
        self.stream_scroll.setYRange(0.5, self.channel_count, padding=0.1)

        self.stream_scroll_time_axis = np.linspace(-5, 0, self.samples * 3)
        self.stream_scroll.setXRange(-5, 0, padding=.005)

        labelStyle = {'color': '#000', 'font-size': '14pt'}
        self.stream_scroll.setLabel('bottom', 'Time', 'Seconds', **labelStyle)
        self.stream_scroll.setLabel('left', 'Channel', **labelStyle)
        color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                      (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
                      (0, 0, 0), (255, 0, 0)]

        for i in range(self.channel_count - 1, -1, -1):
            self.filtered_data[i] = matlib.repmat([0], self.samples * 3, 1).T.ravel()
            self.curves['curve_channel{}'.format(i + 1)] = self.stream_scroll.plot(pen=color_list[i])
            self.curves['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis, y=(
                [point + i + 1 for point in self.filtered_data[i]]))
        # print(len(self.data_buffer))
        self.set_layout()

    def set_layout(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.stream_scroll, 0, 0)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot('PyQt_PyObject')
    def update_plot(self, data):
        # print("原始eeg", data)
        self.filtered_data = np.hstack((self.filtered_data,data))
        self.filtered_data = self.filtered_data[:,self.samples:]
        # 对数据进行fit(求训练数据集的均值，方差，最大值，最小值,这些训练集X固有的属性)transform(归一化)
        data = self.min_max_scaler.fit_transform(self.filtered_data.transpose()).transpose()
        for i in range(self.channel_count):
            current = [(point + i + 1) for point in data[i]]
            self.curves['curve_channel{}'.format(i + 1)].setData(x=self.stream_scroll_time_axis,
                                                                 y=([point for point in current]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = board1()
    ex.show()
    sys.exit(app.exec_())
