import sys
from collections import OrderedDict, deque

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QComboBox, QStackedWidget, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QVBoxLayout, QApplication, QFrame


class game(QWidget):

    def __init__(self):
        super().__init__()
        self.game_interface()

    def game_interface(self):
        # 第一层
        self.game_layout = QGridLayout()
        game_label = QLabel('脑控游戏')
        game_label.setFont(QFont("Microsoft YaHei", 20, 50))
        self.game_01 = QPushButton()
        self.game_01.setStyleSheet("QPushButton{border-image: url(E:/学习/test_platform/Hardware_software_testing/png/"
                                   "虚拟无人机.png)}")
        self.game_01.setFixedSize(400, 200)
        self.game_02 = QPushButton()
        self.game_02.setStyleSheet("QPushButton{border-image: url(E:/学习/test_platform/Hardware_software_testing/png/"
                                   "虚拟小车.png)}" "QPushButton{border:5px}")
        self.game_02.setFixedSize(400, 200)
        self.game_03 = QPushButton()
        self.game_03.setStyleSheet("QPushButton{border-image: url(E:/学习/test_platform/Hardware_software_testing/png/"
                                   "无人机1.jpg)}" "QPushButton{border:5px}")
        self.game_03.setFixedSize(400, 200)
        self.game_04 = QPushButton()
        self.game_04.setStyleSheet("QPushButton{border-image: url(E:/学习/test_platform/Hardware_software_testing/png/"
                                   "小车.jpg)}" "QPushButton{border:5px}")
        self.game_04.setFixedSize(400, 200)

        verticalLine0 = QFrame()
        verticalLine0.setFrameShape(QFrame().HLine)
        verticalLine0.setFrameShadow(QFrame().Sunken)

        verticalLine1 = QFrame()
        verticalLine1.setFrameShape(QFrame().HLine)
        verticalLine1.setFrameShadow(QFrame().Sunken)

        self.game_layout.addWidget(game_label, 0, 17, 1, 2)
        self.game_layout.addWidget(verticalLine0, 1, 0, 1, 40)
        self.game_layout.addWidget(self.game_01, 2, 3, 2, 20)
        self.game_layout.addWidget(self.game_02, 2, 19, 2, 20)
        self.game_layout.addWidget(self.game_03, 5, 3, 2, 20)
        self.game_layout.addWidget(self.game_04, 5, 19, 2, 20)

        self.setLayout(self.game_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = game()
    ex.show()
    sys.exit(app.exec_())
