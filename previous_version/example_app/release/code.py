#!/usr/bin/env python3


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
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
    self.setGeometry(100, 100, 500, 500)
    self.setWindowTitle('somewhere')
    self.score = QLabel(' ', self)
    button_1 = QPushButton('ЖМИ!!!!', self)
    button_1.setGeometry(50, 50, 300, 300)
    self.score.move(50, 0)
    button_1.clicked.connect(self.counter)
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
  sys.exit(app.exec_())
