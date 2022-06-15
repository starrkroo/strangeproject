#!/usr/bin/env python3

'''
  >>> k[0]
  id

  >>> k[1]
  vk_id

  >>> k[2]
  online

  >>> k[3]
  first_name

  >>> k[4]
  second_name

  >>> k[5]
  increaseEarning

  >>> k[6]
  coin
  
  >>> k[7]
  clicks
  
  >>> k[8]
  is_admin # sys_admin, who follow the internet

  >>> k[9]
  is_prepod # is teacher

  >>> k[10]
  is_core # director

'''


from sqlite3 import connect
from os import getcwd
import vk_api
from time import sleep, time
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup as bs4
import requests
from huepy import *

# NOTE: write function which deletes user account


try:
  with open('{}/Logs/conditions.txt'.format(getcwd())) as f:
    item = f.readlines()
    conditions = item
    count_of_conditions = int(item[-1].split(')')[0]) + 1
    del item
except:
  conditions = ''
  count_of_conditions = 1

conn = connect('token.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM ttoken""")

token = cursor.fetchall()[0][0] # token
cursor.close()

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

from Logs.current_version.version import VERSION
with open('Logs/news/information_about_news.txt') as f:
  __changes__ = f.read()

def write_msg(user_id, message):
  try:
    # NOTE: uncomment that whenever you want
    #sleep(1.5)
    directed = int(time())
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': (directed)})
  except Exception as e:
    print(e)

from kvantoDB import Work
database = Work()


with open('Logs/current_version/version.py') as f:
  VERSION = str(f.read())

# registrating our bot
vk = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk)

from time import ctime
current_date = int(ctime().split(' ')[2])

def getNameById(id):
  item = bs4(requests.get('https://vk.com/id{}'.format(str(id))).text, 'lxml').find('body').find('div', class_='pp_cont').find('h2', class_='op_header').text
  return item.split(' ')[0], item.split(' ')[1]

def information():
  return \
    '''
      Команды для Админов:
        /changePriceList <addText> - добавляет в текущий прайс новые условия (/getPriceList)
        /setNewUser <name> <surname> <vk_id> <kCoins> - добавить нового Админа;
        /setNewCore <name> <id> - set new admin
        /givekCoin <name> <how_many> - наградить kCoin'нами;
        /removeUser <name> <id> - удалять если вдруг кто то зарегал второй акк
        /transac <from> <to> <how_many> - функция для перекидывания койной
        /takekCoin <user_id> <how_many> - забрать kCoin'ы;
        /getUsers  выводить данные обо всех пользователях
        /getCores  - получение информации о корах
        /increaseEarning <user_id> <how_many> - уви
        /findUser <user_id>
        /writeEveryBody <text>
        /Version changes - /Version - returns current version; flag <changes> returns changes in current version
    '''

# писать имена через пробел
def information_for_user():
  with open('{}/Logs/conditions.txt'.format(getcwd())) as f:
    return f.read()


def isUser(current):
  try:
    for k in database.get_data():
      if int(current) == k[1]: # current id is in db
        if not bool(int(k[8])) or not bool(int(k[9])) or not bool(int(k[10])): # there is no rules for user
          return True
    return False
  except Exception as e:
    write_msg(event.user_id, '[!] Error: {}'.format(e))

def isCore(current):
  try:
    for k in database.get_data():
      if str(current) == str(k[1]): # current id is in db
        if bool(int(k[9])): # is_core -> [9]
          return True
    return False
  except:
    pass

  


def main():
  for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

      request = event.text
      
      try:    first_user_sent_data  = request.split(' ')[1]
      except: first_user_sent_data = ''
      try:    second_user_sent_data = request.split(' ')[2]
      except: second_user_sent_data = ''
      try:    third_user_sent_data  = request.split(' ')[3]
      except: third_user_sent_data  = ''

      if event.to_me:
        global current_date

        if str(ctime().split(' ')[3]) >= '00:00:00' and int(ctime().split(' ')[2]) > current_date:
          try:
            for k in database.get_data():
              database.update_dataBase(user_id = event.user_id, kCoins = int(k[6]) + int(k[5]), everyDay = True)
          except Exception as e:
            print('Error: {}'.format(e))

          current_date = int(current_date) + 1; 
          print(current_date); 

        # if user is core
        if isCore(event.user_id):
            if '/changePriceList' in request:
              global count_of_conditions
              with open('{}/Logs/conditions.txt'.format(getcwd()), 'a') as f:
                f.write('{}) {};\n'.format(str(int(count_of_conditions)), request.split('/changePriceList')[1]))
              count_of_conditions += 1
            
            elif '/setNewUser' in request:
              try:
                try:
                  database.pushing(first_name = first_user_sent_data, second_name = second_user_sent_data, user_id = third_user_sent_data, user_coins = request.split(' ')[4])
                except:
                  database.pushing(first_name = first_user_sent_data, second_name = second_user_sent_data, user_id = third_user_sent_data)
                write_msg(event.user_id, 'User with datas: \nname: {}\nID: {}\nsuccessfully added!'.format(first_user_sent_data + ' ' + second_user_sent_data, third_user_sent_data))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}\nFollow setted form'.format(e))


##############################################################################
#FIXME: setNewCore делает пользователя кором, даже учитывая то, что он уже зареган в бд
#FIXME: correct adding new cores and new users
##############################################################################


            elif '/setNewCore' in request:
              try:
                database.pushing(first_user_sent_data,  second_user_sent_data, third_user_sent_data, is_core = 1)
                write_msg(event.user_id, 'successfully added')
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/givekCoin' in request:
              try:
                user_coins = database.update_dataBase(user_id = first_user_sent_data, kCoins = second_user_sent_data)
                try: user_coins = int(user_coins)
                except: write_msg(event.user_id, user_coins); continue
                write_msg(event.user_id, 'Now, user vk.com/id{} has {} coins'.format(first_user_sent_data, user_coins))
                write_msg(first_user_sent_data, 'Core gave to you {} coins'.format(user_coins))

                # NOTE: sending information to a user
                for k in database.get_data():
                  if str(first_user_sent_data) == str(k[1]):
                    write_msg(str(k[1]), 'Core gave you kCoins!\nNow you have <{}> kCoins - given {}'.format(user_coins, second_user_sent_data))

              except Exception as e:
                write_msg(event.user_id, 'Please, check formed query\nError: {}'.format(e))

            elif '/deleteCore' in request:
              try:
                database.deleteThis(first_user_sent_data)
              except Exception as e:
                write_msg(event.user_id, 'Error:  follow setted form\n {}'.format(e))
            
            elif '/transac' in request:
              # NOTE: using ids to update data
              try:
                first_user_coins  = database.update_dataBase(user_id = first_user_sent_data, kCoins = - abs(int(third_user_sent_data)))
                second_user_coins =database.update_dataBase(user_id = second_user_sent_data, kCoins = abs(int(third_user_sent_data)))
                write_msg(event.user_id, 'vk.com/id{} has {} coins\nvk.com/id{} has {} coins'.format(first_user_sent_data, first_user_coins, second_user_sent_data, second_user_coins))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: follow setted form\n{}'.format(e))
            elif '/takekCoin' in request:
              try:
                user_coins = database.update_dataBase(user_id = first_user_sent_data, kCoins = - abs(int(second_user_sent_data)))
                write_msg(event.user_id, 'KCoins uploaded!\n{}: {} kCoins'.format(first_user_sent_data, user_coins))
                write_msg(first_user_sent_data, 'Core took from you {} coins'.format(user_coins))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e)) 
            
            elif '/getUsers' in request:
              try:
                list_of_users = ''
                for k in database.get_data():
                  if isUser(k[1]):
                    list_of_users += '{} {} -> (vk.com/id{}) and has {} coins\n'.format(k[3], k[4], k[1], k[6])
                write_msg(event.user_id, list_of_users)
                del list_of_users
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/getCores' in request:
              try:  
                list_of_cores = ''
                for k in database.get_data():
                  if isCore(k[1]):
                    list_of_cores += '{} {} -> (vk.com/id{})\n'.format(k[3], k[4], k[1])
                write_msg(event.user_id, list_of_cores)
                del list_of_cores
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/increaseEarning' in request:
              try:
                try: first_user_sent_data = int(first_user_sent_data)
                except: write_msg(event.user_id, "[!] Error: follow setted form"); continue
                if database.isUserCreated(user_id = first_user_sent_data)[0]:
                  database.update_dataBase(user_id = first_user_sent_data, increaseEarning = second_user_sent_data)
                  write_msg(event.user_id, 'Now user <{}> has {} of increaseEarning'.format(first_user_sent_data, second_user_sent_data))
                else:
                  write_msg(event.user_id, 'There is no user vk.com/id{}'.format(first_user_sent_data))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))
            
            elif '/findUser' in request:
              try:
                try: first_user_sent_data = int(first_user_sent_data)
                except: write_msg(event.user_id, '[!] Error: your first parameter is a string'); continue
                data = database.outputing(user_id = first_user_sent_data)
                write_msg(event.user_id, 'Vk id: vk.com/id{}\n Name: {}\nSurname: {}\nIncreaseEarning: {}\nCoins: {}\n'.format(data[0], data[1], data[2], data[3], data[4]))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/writeEveryBody' in request:
              try:
                for k in database.get_data():
                  write_msg(k[1], str(request.split('/writeEveryBody')[1].strip()))
              except Exception as e:
                write_msg(event.user_id, '[!] Error: {}'.format(e))

            elif '/Version' in request:
              if 'changes' in request:
                write_msg(event.user_id, __changes__)
                continue
    
              write_msg(event.user_id, 'Current version -> {}'.format(VERSION))


#NOTE: realize that core is taking or giviing or upping increaseearnin to user
              

            else:
              write_msg(event.user_id, information())


        # if user want to get registrated
        elif '/register' in request:
          first_name = getNameById(event.user_id)[0]
          last_name  = getNameById(event.user_id)[1]

          try:
            database.pushing(first_name, last_name, event.user_id)
            write_msg(event.user_id, "successfully created!\nNow you\n{} {}: {}".format(first_name, last_name, event.user_id))
          except Exception as e:
            write_msg(event.user_id, '[!] Error: {}'.format(e))

        # if user is nobody
        elif not isCore(event.user_id) or not isUser(event.user_id):
          write_msg(event.user_id, 'You need to create account\nWrite: /register to create it')

        # if user is user)
        elif isUser(event.user_id):
          write_msg(event.user_id, 'hello, nobody')

    

if __name__ == '__main__':
  main()

