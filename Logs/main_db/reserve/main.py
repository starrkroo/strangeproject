#!/usr/bin/env python3

from sqlite3 import connect
import vk_api
from time import sleep, time
from vk_api.longpoll import VkLongPoll, VkEventType

conn = connect('token.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM ttoken""")

token = cursor.fetchall()[0][0] # token
cursor.close()

VERSION = 'Beta- KvantoCoins 1.13'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
  try:
    sleep(1.5)
    directed = int(time())
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': (directed)})
  except Exception as e:
    print(e)

database = 


with open('Logs/current_version/version.py') as f:
  VERSION = f.read()

# registrating our bot
vk = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk)

from time import ctime
current_date = ctime().split(' ')[2]


def isUser(current):
  try:
    for k in 

