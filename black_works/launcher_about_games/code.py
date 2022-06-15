#!/usr/bin/env python3

# create a finder -> how?

# 1 kcoin = 0.7 of ruble

# если пользователь купил игру - койны за игру идут админу игры

# should get an image for game

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

# автоматически в массив значений уникального кода вносить у удалять ключи если пользователь уже ввел определенный ключ
# выдавать пользователю определенный unique code который у меня на сервере будет сгенерирован уже и выдавать ему право игра в игру давая ссылку на скачивание
# data, where is the data? where is whole games?

class My_GUI(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    grid = QGridLayout()
    grid.setSpacing(10)

    self.button = QPushButton('ЖМИ!!!!')
    grid.addWidget(self.button)

    self.button.setStyleSheet("background-color: black;")
    self.button.clicked.connect(self.another)

    self.setLayout(grid)
    self.setWindowTitle('somewhere')
    self.setGeometry(100, 100, 850, 850)
    self.show()

  def another(self):
    print('hell oworld')


if __name__ == '__main__':
  app = QApplication(sys.argv)
  my_window = My_GUI()
  #my_window.showFullScreen()
  sys.exit(app.exec_())
