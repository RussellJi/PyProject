import sys
from collections import OrderedDict, deque

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QComboBox, QStackedWidget, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QVBoxLayout, QApplication, QFrame
import pyqtgraph as pg
import numpy as np
from numpy import matlib


class model(QWidget):

    def __init__(self):
        super().__init__()
        self.model_interface()

    def model_interface(self):
        # 第一层
        self.model_layout = QGridLayout()
        model_label = QLabel('脑电分类模型')
        model_label.setFont(QFont("Microsoft YaHei", 20, 50))
        self.model_01 = QPushButton("CCA_4分类")
        self.model_01.setStyleSheet("background-color:lightblue")
        self.model_01.setFont(QFont("Microsoft YaHei", 18, 50))
        self.model_01.setFixedSize(250, 200)
        self.model_02 = QPushButton("CCA_10分类")
        self.model_02.setStyleSheet("background-color:lightblue")
        self.model_02.setFont(QFont("Microsoft YaHei", 18, 50))
        self.model_02.setFixedSize(250, 200)
        self.model_03 = QPushButton("谱估计(CNN)4分类")
        self.model_03.setStyleSheet("background-color:lightblue")
        self.model_03.setFont(QFont("Microsoft YaHei", 18, 50))
        self.model_03.setFixedSize(250, 200)
        self.model_04 = QPushButton("复杂谱(CNN)4分类")
        self.model_04.setStyleSheet("background-color:lightblue")
        self.model_04.setFont(QFont("Microsoft YaHei", 18, 50))
        self.model_04.setFixedSize(250, 200)
        self.model_05 = QPushButton("幅度谱(CNN)4分类")
        self.model_05.setStyleSheet("background-color:lightblue")
        self.model_05.setFont(QFont("Microsoft YaHei", 18, 50))
        self.model_05.setFixedSize(250, 200)
        self.model_06 = QPushButton()
        self.model_06.setStyleSheet("QPushButton{border-image: url(E:/学习/test_platform/Hardware_software_testing/png/"
                                    "加.jpg)}")
        self.model_06.setFixedSize(250, 200)

        verticalLine0 = QFrame()
        verticalLine0.setFrameShape(QFrame().HLine)
        verticalLine0.setFrameShadow(QFrame().Sunken)

        verticalLine1 = QFrame()
        verticalLine1.setFrameShape(QFrame().HLine)
        verticalLine1.setFrameShadow(QFrame().Sunken)

        self.model_layout.addWidget(model_label, 0, 17, 1, 2)
        self.model_layout.addWidget(verticalLine0, 1, 0, 1, 40)
        self.model_layout.addWidget(self.model_01, 2, 3, 2, 10)
        self.model_layout.addWidget(self.model_02, 2, 15, 2, 10)
        self.model_layout.addWidget(self.model_03, 2, 23, 2, 10)
        self.model_layout.addWidget(self.model_04, 5, 3, 2, 10)
        self.model_layout.addWidget(self.model_05, 5, 15, 2, 10)
        self.model_layout.addWidget(self.model_06, 5, 23, 2, 10)

        self.setLayout(self.model_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = model()
    ex.show()
    sys.exit(app.exec_())
