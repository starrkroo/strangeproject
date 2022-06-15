#!/usr/bin/env python3


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from sqlite3 import connect
from huepy import *

counter_var = 0

def counter_var_setting():
  global counter_var
  cursor = connect('data.db').cursor()
  cursor.execute('SELECT * FROM Data')
  counter_var = int(cursor.fetchall()[-1][0])

def setting_default_value():
  conn = connect('data.db')
  cursor = conn.cursor()
  
  try:
    cursor.execute("CREATE TABLE Data (code TEXT)")
  except: pass
  cursor.executemany('INSERT INTO Data VALUES(?)', '0')
  conn.commit()
  cursor.close()
  conn.close()

class My_GUI(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):

    grid = QGridLayout()
    grid.setSpacing(5)

    self.score = QLabel(' ')
    grid.addWidget(self.score, 1, 1)

    self.button = QPushButton('ЖМИ!!!!')
    grid.addWidget(self.button, 1, 2)

    self.button.setGeometry(0,0, 200, 200)
    self.button.clicked.connect(self.counter)

    self.setLayout(grid)
    self.setWindowTitle('somewhere')
    self.setGeometry(100, 100, 500, 500)
    self.show()
  def counter(self):
    global counter_var
    counter_var += 1
    self.score.setText(str(counter_var))
    print(counter_var)
    conn = connect('data.db')
    cursor = conn.cursor()
    try:
      cursor.execute("CREATE TABLE Data (code INT)")
    except:
      pass
    cursor.execute('INSERT INTO Data VALUES(?)', ([counter_var]))
    cursor.execute('SELECT * FROM Data')

    conn.commit()
    cursor.close()
    conn.close()
    
    
  
if __name__ == '__main__':
  try:
    counter_var_setting()
  except:
    setting_default_value()
  app = QApplication(sys.argv)
  my_window = My_GUI()
  #my_window.showFullScreen()
  sys.exit(app.exec_())
