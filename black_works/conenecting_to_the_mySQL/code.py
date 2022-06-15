#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

#host: 'remotemysql.com', 
#user:'dAEwLGf27F', 
#password:'rnfA4rQCxA', 
#database: 'dAEwLGf27F'


def connect():
  conn = mysql.connector.connect(
    host = 'remotemysql.com', 
    user ='dAEwLGf27F', 
    password ='rnfA4rQCxA', 
    database = 'dAEwLGf27F')
  cursor = conn.cursor(buffered=True)

  cursor.execute("SHOW COLUMNS FROM users")
  for index,k in enumerate(cursor.fetchall()):
    print('{}) {}'.format(index, k[0]))

#  query = 'update users set coin = %s where first_name = %s'
#  
#  cursor.execute(query, (5, 'testing'))
#  conn.commit()


#  cursor.execute("SELECT * FROM users")
#  for k in (cursor.fetchall()):
#    print(k)

#cursor.execute("SELECT * FROM users")
#  for k in (cursor.fetchall()):
#    print(k)

# users, register, market, buys



# vk_id, first_name, last_name, coin, clicks, is_admin, is_prepod, is_core, code_invate, user_ip, reg
# is_core - director
# is_admin - VIP
# is_prepod - keki

# reg, 0, 1, 3( deleted, registed, blocked )
  query = '''INSERT INTO users (
        vk_id,
        first_name, 
        last_name, 
        online, 
        coin, 
        clicks, 
        is_admin,
        is_prepod, 
        is_core, 
        code_invate,
        user_ip,
        reg)
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
  #cursor.execute(query, (7777777, 'omar', 'starrk', 0, 123, 456, 0, 0, 0, '123123', '7777777', 1))
  #conn.commit()
  cursor.close()
  conn.close()

if __name__ == '__main__':
    connect()
