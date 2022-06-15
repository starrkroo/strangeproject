#!/usr/bin/env python3


import mysql.connector
from os import getcwd
from huepy import *

# NOTE: wrote ---> pushing, outputing, isUserCreated, drop_database, write method which will print me what I want method(first_name, user_id, query='increaseEarning'), update_dataBase, 
# NOTE: should write --> delete_data; delete_user -> same

class Work:
  def __init__(self):
    try:
      self.connect = mysql.connector.connect(
        host     = 'remotemysql.com',
        user     = 'dAEwLGf27F',
        password = 'rnfA4rQCxA',
        database = 'dAEwLGf27F'
        )
      self.cursor = self.connect.cursor()

    except:
      print("Bad self.connection..")
      exit()


  def create_database(self):
    self.cursor.execute('''CREATE TABLE users (
        id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
        vk_id BIGINT(20),
        online INT(3),
        first_name TEXT,
        last_name TEXT,
        increaseEarning INT(16),
        coin BIGINT(255),
        clicks BIGINT(255),
        is_admin INT(1),
        is_prepod INT(3),
        is_core INT(3),
        code_invate TEXT,
        user_ip TEXT,
        reg INT(2))
    ''')
    self.connect.commit()

  def getValue(self, first_name, query):
    self.cursor.execute('SHOW COLUMNS FROM users')
    commands = []
    try:
      for k in self.cursor.fetchall():
        commands.append(k[0])

      for k in self.get_data():
        if str(first_name) == k[3]:
          return k[commands.index(query)]
    except Exception as e:
      raise('Error: {}'.format(e))

  def isUserCreated(self, first_name, second_name = False, user_id = False):
    for k in self.get_data():
      # print('{} in {}\n{} in {}\n{} in {}'.format(first_name, k[3], second_name, k[4], user_id, k[1]))
      if user_id and user_id != '':
        if str(user_id)  == str(k[1]):
          return True, k[0]
      if second_name and second_name != '':
        if first_name == k[3] or second_name == k[4]:
          return True, k[0]
      if first_name == k[3] or second_name == k[4]:
        return True, k[0]
    return False, None

  def get_data(self):
    try:
      self.cursor.execute('SELECT * FROM users')
      return self.cursor.fetchall()
    except Exception as e:
      self.create_database()
      print((str(e) + orange('\nTrying to create it..')))
      self.cursor.execute('SELECT * FROM users')

      return self.cursor.fetchall()
 
  # like a modification for outputing value (yes, it checks only by first_name((( ) NOTE: can actually delete this method cuz this item using only in local working [153, 154]
  def outputing(self, first_name = False, user_id = False):
    try:
      self.cursor.execute("SELECT * FROM users")
    except Exception as e:
      return e

    sht = self.cursor.fetchall()
    for index, data in enumerate(sht):
      if first_name == 'all':
        # list  
        return sht
      else: 
        if first_name in data[3]:
          # tuple
          return sht[index]

  def deleteThis(self, user_id, isAll = False):
    if isAll:
      for index, k in enumerate(self.get_data()):
        print(k)
        self.cursor.execute('DELETE FROM users WHERE first_name = %s', (k[3],))

    # if first_name and (first_name != ''):
    #   for k in self.get_data():
    #     #print('{} in {} = {}'.format(name, k, name in k))
    #     if str(first_name) == str(k[3]):
    #       self.cursor.execute('DELETE FROM users WHERE name = ?', (first_name,))
    #if user_id and (user_id != ''):
    for k in self.get_data():
      #print('{} == {} = {}'.format(id, k[1], id == k[1]))
      if str(user_id) == str(k[1]):
        self.cursor.execute('DELETE FROM users WHERE vk_id = %s', (user_id,))

  def update_dataBase(self, first_name, kCoins = False, increaseEarning = False, everyDay = False):

    # first_name - to indentify user

    if kCoins and (kCoins != ''):
      try: isRunning = isinstance(int(kCoins), int)
      except: raise Exception("You are usersing not with integer..")
      #if (kCoins).split('.')[0].isdigit():
      if isRunning:
        for index, k in enumerate(self.get_data()):
          if str(first_name) == str(k[3]):
            if everyDay:
              self.cursor.execute('UPDATE users SET coin = %s WHERE first_name = %s', (kCoins, first_name)); self.connect.commit()
            else:
              self.cursor.execute('UPDATE users SET coin = %s WHERE first_name = %s', (str(int(self.get_data()[index][6]) + int(kCoins)), first_name)); self.connect.commit()
              return (str(int(self.get_data()[index][6])))

    elif increaseEarning and increaseEarning != '':
      try: isRunning = isinstance(int(increaseEarning), int)
      except: raise Exception('Your are working not with integer..')
      if isRunning:
        for index, k in enumerate(self.get_data()):
          if first_name in k[3]:
            self.cursor.execute('UPDATE users SET increaseEarning = %s WHERE first_name = %s', (str(int(self.get_data()[index][5]) + int(increaseEarning)), first_name)); self.connect.commit()
            return (str(int(self.get_data()[index][6])))
    else:
      return 'Comon boy, it is not funny, write values!'

  def drop_dataBase(self):
    try:
      self.cursor.execute("DROP TABLE users")
      self.connect.commit()
      return green('Succeed')
    except:
      print("already deleted")


  def pushing(self, first_name, second_name, user_id = False, user_coins = False, increaseEarning = False, error = False):
    if error:
      raise Exception('User alredy created')
    query = """INSERT INTO users(
      vk_id, 
      online, 
      first_name,
      last_name,
      increaseEarning,
      coin,
      clicks,
      is_admin,
      is_prepod, 
      is_core, 
      code_invate,
      user_ip,
      reg            ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


    # 2 stuffs which block spamming pushing datas
    if not len(user_id):
      return 'Print user ID!'
    if not len(first_name) and not len(second_name):
      return 'Print user Name!'

    datas = self.isUserCreated(first_name, second_name, user_id)
    try:
      if datas[0]:
       print('Oh shit. User with datas: \nusername: {}\nvk_id: {}\n\talredy created with ID <{}>'.format(first_name + ' ' + second_name, user_id, datas[1]))
       self.pushing(0,0, error = True)
    except: pass

    # checks value of user_coins (is that string? if it is then raising an error)
    if user_coins and (user_coins != ''):  
      try:
        user_coins = int(user_coins)
      except:
        raise Exception('Why user_coins - str?\n should be int')
    else:
      user_coins = 0

    # same checking
    if increaseEarning and increaseEarning != '':
      try:
        increaseEarning = int(increaseEarning)
      except:
        raise Exception('Why increaseEarning - str?\nshould be int')
    else:
      increaseEarning = 10

    # main adding
    try:
      self.cursor.execute(query, (user_id, 0, first_name, second_name, increaseEarning, user_coins, 0, 0, 0, 0, 0, 0, 0))
      self.connect.commit()

      return green('Succeed')

    except Exception as e:
      return e

def showing():
  name = input("Your query(can be id) : ")
  if name.isdigit():
    new_data = item.outputing(user_id = name)
  new_data = item.outputing(first_name = name)

  if isinstance(new_data, list): 
    for k in new_data: 
      print(k)
  elif isinstance(new_data, tuple): 
    print(new_data)

def appending():
  first_value     = input("Enter first  name of user: ")
  second_value    = input("Enter second name of user: ")
  user_id         = input("Enter user_id of user: ")
  user_coins      = input("Enter coins of user: ")
  increaseEarning = input("Enter earning of user: ")

  print(item.pushing(first_value, second_value, user_id, user_coins, increaseEarning))

def updating():
  first_name1     = input("Enter name: ")
  kCoins          = input("How many coins <You can pass this>: ")
  increaseEarning = input("Enter count of increaseEarning <this also>: ")

  print(item.update_dataBase(first_name1, kCoins, increaseEarning))

def checking():
  data = (item.isUserCreated(input("Enter first_name: "), input("Enter last_name: "), input("Enter user_id <can pass it>: ")))
  if data[0]:
    print("User is in database!!\nID in db: <{}>".format(data[1]))

def drop_database():
  item.drop_dataBase()

def removeUser():
  desidition = input("Delete whole database? Y/n: ")
  if desidition in ['Y', 'y']:
    item.deleteThis(None, isAll = True)
  else:
    item.deleteThis(input("Enter vk_id: "))

item = Work()
if __name__ == '__main__':
  run = True
  while run:
    try:
      choice = input("[S]how or [A]ppend or [R]emove or [U]pdate or [C]heck or [D]ropDatabase or [E]xit: \n")
      if choice in ['E', 'e']:
        run = False
      elif choice in ['S', 's']:
        showing()
      elif choice in ['A', 'a']:
        appending()
      elif choice in ['R', 'r']:
        removeUser()  
      elif choice in ['U', 'u']:
        updating()
      elif choice in ['C', 'c']:
        checking()
      elif choice in ['D', 'd']:
        drop_database()
    except KeyboardInterrupt:
      exit()




