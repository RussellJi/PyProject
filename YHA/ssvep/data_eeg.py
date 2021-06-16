import gzip
import pickle
import time
import scipy.io as sio
import numpy as np
from numpy import matlib
from sklearn.model_selection import train_test_split
# from tensorflow.python.keras.utils.np_utils import to_categorical

import press1 as pre
from PyQt5.QtCore import QThread, pyqtSignal
from brainflow import BrainFlowInputParams, BoardShim
from processing import step_1, step_2
from feature import extration


class MyThread(QThread):  # 线程类
    org_signal = pyqtSignal(object)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    pre_signal = pyqtSignal(object)
    feature_signal = pyqtSignal(object)
    command_signal = pyqtSignal(str)

    def __init__(self, board_set, pre_set, class_set):
        super(MyThread, self).__init__()
        self.board_set = board_set
        # print(self.board_set)
        self.processing_step1 = step_1()
        self.processing_step2 = step_2()
        self.pre_set = pre_set
        self.feature = extration()
        self.class_set = class_set
        self.is_on = True
        self.puanduan1 = False
        self.puanduan2 = False
        self.puanduan3 = False

    def run(self):  # 线程执行函数
        params = BrainFlowInputParams()
        board_id = self.board_set[0]
        self.c_value = []

        params.serial_port = self.board_set[1]
        self.board = BoardShim(board_id, params)
        # 在线数据

        #一导联数据和量导联数据

        self.board.prepare_session()
        self.board.start_stream()
        time.sleep(3)
        n = 1
        while self.is_on:

            time.sleep(2)
            data = self.board.get_current_board_data(self.board_set[3])
            data = data[1:9]
            mean_data = np.tile(data.mean(axis=1).reshape(8, 1), (1, self.board_set[3]))
            # print(data.shape)
            data = data - mean_data


            if self.puanduan1:
                self.org_signal.emit(data)
            filter1_data = self.processing_step1.step_1_list[self.pre_set[0][0]](data, self.pre_set[0])
            filter2_data = self.processing_step2.step_2_list[self.pre_set[1][0]](filter1_data, self.pre_set[1])
            if self.puanduan2:
                # print(self.pre_set)
                self.pre_signal.emit(filter2_data)
            feature_data = self.feature.feature_list[self.class_set[0]](filter2_data, self.class_set)
            # print(np.argmax(feature_data))
            if self.puanduan3:
                self.feature_signal.emit(feature_data)
                # print(feature_data)
            result = np.argmax(feature_data)

            r = feature_data[result]


            if result == 5 :
                r = r + 0.1
            elif result == 6:
                r = r + 0.05

            if r > 0.4 :
                print("分类结果：", result + 1)
                b = str(result + 1)
                self.command_signal.emit(b)




