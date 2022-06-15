#!/usr/bin/env python3

# realize that client has registrated on your teacher

import requests
from bs4 import BeautifulSoup as bs4

from os import getcwd
try:
  with open('{}/Logs/conditions.txt'.format(getcwd())) as f:
    conditions = f.readlines()
except:
  conditions = ''
count_of_conditions = 1

import mysql.connector
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

conn = connect('Logs/token/token.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM ttoken""")
token = cursor.fetchall()[0][0] # token
cursor.close()



dbs_data = mysql.conector.connect(
      conn = mysql.connector.connect(
      host = 'remotemysql.com',
      user ='',
      password ='',
      database = '')
)
cursor = dbs_data.cursor()

# X.Y.Z -> 
#   X - координальное изменение проекта
#   Y - при изменении, возможно добавлении функциональности
#   Z - при исправлении небольших багов
# x.x1x2
VERSION = 'Beta- KvantoCoins 1.13'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

from Logs.users.code import Working
data_user = Working()

from Logs.cores.code import Working
data_core = Working()

from time import time, ctime, sleep
current_date = ctime().split(' ')[2]

def getNameById(id):
  return bs4(requests.get('https://vk.com/id{}'.format(str(id))).text, 'lxml').find('body').find('div', class_='pp_cont').find('h2', class_='op_header').text.replace(' ', '_')

def write_msg(user_id, message):
    try:
      sleep(1.5)
      directed = int(time())
      vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': (directed)})
    except Exception as e:
      print(e)


# Checking for user
def isUser(current):
  try:
    for k in data_user.get_data():
      if str(current) == k[2]:
        return True
    return False
  except Exception as e:
    write_msg(current, '[!] Error: {}'.format(e))

# Checking for core
def isCore(current):
  try:
    for k in data_core.get_data:
      if str(current) == k[2]:
        return True

    return False
  except:
    pass
    # print(("there is no database"))

# Giving information about commands
def information():
  return \
    '''
      Команды для Админов:
        /changePriceList <addText> - добавляет в текущий прайс новые условия (/getPriceList)
        /setNewUser <name> <id> <kCoins> - добавить нового Админа;
        /changeUserName <from> <to>  - поменять имя пользователя с new_user_1567884575234 на Имечко_Фамилия
        /setNewCore <name> <id> - set new admin
        /givekCoin <name> <how_many> - наградить kCoin'нами;
        /removeUser <name> <id> - удалять если вдруг кто то зарегал второй акк
        /transac <from> <to> <how_many> - функция для перекидывания койной
        /takekCoin <name> <how_many> - забрать kCoin'ы;
        /getUsers                    - выводить данные обо всех пользователях
        /getCores                    - получение информации о корах
        /increaseEarning <name> <how_many> - уви
        /findUser <findname>
        /writeEveryBody <text>
        /Version changes - /Version - returns current version; flag <changes> returns changes in current version
    '''

# писать имена через пробел

def information_for_user():
  with open('{}/Logs/conditions.txt'.format(getcwd())) as f:
    return f.read()


def main():
  try:
    for event in longpoll.listen():
      if event.type == VkEventType.MESSAGE_NEW:
        request = event.text

        try:
          first_user_sent_data = request.split(' ')[1]
          second_user_sent_data = request.split(' ')[2]
        except:
          pass



        if event.to_me:
          global current_date
          current_date = 25

          #print('[{}]: <{}>: {}'.format(ctime().split(' ')[3], getNameById(event.user_id), request))
  
          #print('{} > {} => {}'.format(int(ctime().split(' ')[2]), current_date, int(ctime().split(' ')[2]) > current_date))

          #                                               next_dat                   > previous_day       -> means that came another next day
          if str(ctime().split(' ')[3]) >= '00:00:00' and int(ctime().split(' ')[2]) > current_date:
            try:
              for k in data_user.get_data(): # gets names            
                data_user.update_dataBase(first_name = k[1], kCoins = int(k[3]) + int(k[4]), everyDay = True)
            except Exception as e:
              print('Error: {}'.format(e))

            current_date = int(current_date) + 1; 
            print(current_date); 

          # print('{} < {}'.format(current_date, ctime().split(' ')[2]))

          # check for core, user, not user not core, user or core

          if '/register' in request:
            try:
              #name = 'new_user_{}'.format(int(time()))
              name = getNameById(event.user_id)
              data_user.pushing(name, event.user_id)
              write_msg(event.user_id, "successfully created!\nNow you\n{}: {}".format(name, event.user_id))
            except Exception as e:
              write_msg(event.user_id, '[!] Error: {}'.format(e))


  # isNobody
          if not isUser(event.user_id) and not isCore(event.user_id):
            write_msg(event.user_id, 'You need to create account\nWrite: /register to create it')

  # isUserAndCore
          elif isUser(event.user_id) and isCore(event.user_id):
            try:
              write_msg(event.user_id, 'Found you in users.database and in cores.database.. \ndeleteting in users.database')
              data_user.delete_data(id = str(event.user_id))
            except Exception as e:
              write_msg(event.user_id, '[!] Error: {}'.format(e))


  # isCore
          elif isCore(event.user_id):

  # /changePriceList <text>
            if '/changePriceList' in request:
              global count_of_conditions
              with open('{}/Logs/conditions.txt'.format(getcwd()), 'a') as f:
                f.write('{}) {};\n'.format(str(int(count_of_conditions)), request.split('/changePriceList')[1]))
              count_of_conditions += 1

  # /setNewUser <name> <id> <kCoins>
            elif '/setNewUser' in request:
              try:
                try:
                  data_user.pushing(first_user_sent_data, second_user_sent_data, request.split(' ')[3])
                except:
                  data_user.pushing(first_user_sent_data, second_user_sent_data)
                write_msg(event.user_id, 'User with datas: \nname: {}\nID: {}\nsuccessfully added!'.format(first_user_sent_data, second_user_sent_data))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}\n'.format(e))

  #/changeUserName <from> <to>
            elif '/changeUserName' in request:
              # нужно проверить есть ли пользователь в базе данных
              try:
                if data_user.isUserCreated(first_user_sent_data, second_user_sent_data):
                  data_user.update_dataBase(first_name = first_user_sent_data, swap_name = second_user_sent_data)
                  write_msg(event.user_id, "User's datas successfully changed!\n\nfrom: {}\nto: {}".format(first_user_sent_data, second_user_sent_data))
                else:
                  write_msg(event.user_id, "There is no user {}".format(first_user_sent_data))
              except Exception as e:
                # there is no user
                  write_msg(event.user_id, '[!] Error: {}'.format(e))

  # /setNewCore <name> <id>
            elif '/setNewCore' in request:
              try:
                data_core.pushing(first_user_sent_data, second_user_sent_data)
                write_msg(event.user_id, 'Core with datas: \nname: {}\nID: {}\nsuccessfully added!'.format(first_user_sent_data, second_user_sent_data))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}\n'.format(e))

  # /givekCoin <name> <how_many>
            elif '/givekCoin' in request:
              try:
                user_coins = data_user.update_dataBase(first_name = first_user_sent_data, kCoins = second_user_sent_data)
                write_msg(event.user_id, 'KCoins uploaded!\n{}: {} kCoins'.format(first_user_sent_data, user_coins))

                for k in data_user.get_data():
                  if str(first_user_sent_data) == str(k[1]):
                    write_msg(str(k[2]), 'Core gave you kCoins!\nNow you have <{}> kCoins - given {}'.format(user_coins, second_user_sent_data))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))              

  # /deleteCore <name>
            elif '/deleteCore' in request:
              try:
                data_core.delete_data(first_user_sent_data, second_user_sent_data)
                write_msg(event.user_id, 'Core deleted')
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

  # /removeUser <name> <id>
            elif '/removeUser' in request:
              try:
                if data_user.isUserCreated(first_user_sent_data, second_user_sent_data):
                  data_user.delete_data(first_user_sent_data, second_user_sent_data)
                  write_msg(event.user_id, 'User successfully deleted!')
                  write_msg(second_user_sent_data, 'You have deleted..')
                else:
                  write_msg(event.user_id, 'There is no user with next datas: \n{}: vk.com/id{}'.format(first_user_sent_data, second_user_sent_data))
              except:
                write_msg(event.user_id, '<username> <id>')

  # /transac <from> <to> <how_many>
            elif '/transac' in request:
              # забрать койны у одного в значении 200, добавить другому в значении 200
              try:
                first_user = data_user.update_dataBase(first_name = first_user_sent_data, kCoins = str(-int(str(request.split(' ')[3]))))
                second_user = data_user.update_dataBase(first_name = second_user_sent_data, kCoins = (str(request.split(' ')[3])))

                write_msg(event.user_id, 'Now they have: \n{}: {}\n{}: {}'.format(first_user_sent_data, first_user, second_user_sent_data, second_user))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

  # /takekCoin <name> <how_many>
            elif '/takekCoin' in request:
              try:
                user_coins = data_user.update_dataBase(first_name = first_user_sent_data, kCoins = str(-int(second_user_sent_data)))
                write_msg(event.user_id, 'KCoins uploaded!\n{}: {} kCoins'.format(first_user_sent_data, user_coins))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/getUsers' in request:
              try:
                another = ''
                if len(data_user.get_data()) == 0: write_msg(event.user_id, 'There is no users(')
                for index, k in enumerate(data_user.get_data()):
                  another += '{}) {}: vk.com/id{}\n'.format(index+1, k[1], k[2])
                write_msg(event.user_id, str(another))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/getCores' in request:
              try:
                another = ''
                for index, k in enumerate(data_core.get_data):
                  another += '{}) {}: vk.com/id{}\n'.format(index+1, k[1], str(k[2]))
                write_msg(event.user_id, another)
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}\nDatabase is empty.'.format(e))

  # /increaseEarning <name> <how_many>
            #elif '/increaseEarning' in request: # FIXME: fix it

  # /findUser <findname>
            elif '/findUser' in request:
              isFound = False
              try:
                for index, k in enumerate(data_user.get_data()):
                  if str(first_user_sent_data) == str(k[1]) or str(first_user_sent_data) == str(k[2]):
                    write_msg(event.user_id, '{}) {}: vk.com/id{} <{} kCoins>'.format(index+1, k[1], k[2], str(k[3])));
                    isFound = True
                if not isFound:
                  write_msg(event.user_id, 'There is no user {}'.format(first_user_sent_data))
                del isFound
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

  # /writeEveryBody <text>
            elif '/writeEveryBody' in request:
              try:
                for k in data_user.get_data():
                  write_msg(str(k[2]), str(request.split('/writeEveryBody')[1].strip()))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/Version' in request and 'changes' in request:
              with open('{}/Logs/Changes.txt'.format(getcwd())) as f:
                write_msg(event.user_id, f.read())
            elif '/Version' in request:
              try:
                write_msg(event.user_id, VERSION)
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            else:
              write_msg(event.user_id, information())

            # isUser
          elif isUser(event.user_id):
            if '/getkCoin' in request:
              try:
                for k in data_user.get_data():
                  if str(event.user_id) == str(k[2]):
                    write_msg(event.user_id, 'You have {} kCoins'.format(str(k[3]))); break;
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/getFullinfo' in request:
              try:
                for k in data_user.get_data():
                  if str(event.user_id) == str(k[2]):
                    write_msg(event.user_id, '{}: vk.com/id{} <{} kCoins>'.format(str(k[1]), str(k[2]), str(k[3]))); break;
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/Version' in request:
              try:
                write_msg(event.user_id, VERSION)
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))


            else:
              write_msg(event.user_id, information_for_user())

  except: #(requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
        #requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
    print('\n______ERROR TimeOut______')
         



if __name__ == "__main__":
  main()
