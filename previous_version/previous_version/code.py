#!/usr/bin/env python3

# Кванториум - детский технопарк, за поощрения дел которых нужно поощрать ...
# скрыт токен 
# нету возможности в повторении

# create a database
#     input in data base token -> ask password


# постить посты с тех групп на которые подписаны подписчики
# написать на ткинтере работу
# написать сайт (adaptive)
# передавать ккойны на другие аккаунты
# связывать значение данных от компьютера и записывать в базу (левый аккаунт для рассылки)

from sqlite3 import connect
conn = connect('Logs/token/token.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM ttoken""")

token = cursor.fetchall()[0][0]

cursor.close()

from Logs.users.code import Working
item = Working()

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from time import time
from huepy import *


INCREASE_VALUE = 10
users = []
users_using_coins = {}       # -> {'starrk': '221396820'}
kvantorium_users  = {}       # -> {'221396820': '1000'} 
cores = {}

cores.update({"Властелин-кКойнов": '175252007', 'Холоп': '123'}) # 221396820

from time import ctime
def checking():
    with open('Logs/counter.txt', 'w') as f:
        reader = open('Logs/counter.txt') 
        if ctime().split(' ')[2] > reader.read():
            for k in kvantorium_users:
                pass
                #kvantorium_users[k] = str(int(kvantorium_users[k]) + INCREASE_VALUE)
            f.write(ctime().split(' ')[2]); 
        f.close()

def starting_counting(data):
    pass


def write_msg(user_id, message):
    try:
      vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': int(time())})
    except Exception as e:
      print(red(e))

def information():
    return \
    ''' 
        kvantoCoin'ы можно получать:
                1) За посещение уроков.
                2) бебебе еще не придумал

      /name <name> - регистрирует ваше имя в базе
      /getkCoin - получить данные о своем счете;
      /help     - helper
      ////
    '''

def info_for_god():
    return \
  '''
    /setNewUser <name> <id> - добавить нового Админа;
    /setNewCore <name> <id> - set new admin
    /givekCoin <name> <how_many> - наградить kCoin'нами;
    /takekCoin <name> <how_many> - забрать kCoin'ы;
    /getAllUsers                    - выводить данные обо всех пользователях
    /increaseEarning <name> <how_many> - уви
  '''


def checking_for_god(admin):
    if admin in [*cores.values()]:
        return True
    return False

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)


def calling(current):
    #write_msg(cores[current], 'Я слушаю вас, мой повелитель. \nКоманды для вас\n {}'.format(info_for_god()))
    write_msg(current, 'Ччето ты походу намутил здесь братан. Смотри команды еще раз {}'.format(info_for_god()))

def calling_user(current):
    write_msg(current, 'чет не то, davay po novoi! \nCommands:\n {}'.format(information()))

def checking__user(user): # поиск есть ли пользователь в базе
    print('{} in {} = {}'.format(user, [*users_using_coins.keys()], user in [*users_using_coins.keys()]))
    if user in [*users_using_coins.keys()]:
        return True
    return False
def checking__user_id(id): # поиск айди пользователя
    print('{} in {} = {}'.format(id, [*users_using_coins.values()], id in [*users_using_coins.values()]))
    if id in [*users_using_coins.values()]:
        return True
    return False

for event in longpoll.listen():
    #checking()
    if event.type == VkEventType.MESSAGE_NEW:
         # users_using_coins = {}       # -> {'starrk': '221396820'}
         # kvantorium_users  = {}       # -> {'221396820': '1000'}
        if event.user_id not in users:
            users.append(event.user_id)
        if event.to_me:
  
            request = event.text
            
            if checking_for_god(str(event.user_id)):
                print('kvantorium_users - {}'.format(red(kvantorium_users)))
                print('users_using_coins - {}'.format(orange(users_using_coins)))

                splitted = request.split(' ') # ---> /setNewUser somebody something
                try:
                    first    = splitted[1]
                    second   = splitted[2]
                    print('Second data = {}'.format(red(second)))
                except:
                    print()

                if '/setNewUser' in request:
                    try:
                        if checking__user(str(first)) or checking__user_id(str(second)):
                            write_msg(event.user_id, 'User already created!')
                            continue

                        users_using_coins.update({first: second})
                        write_msg(event.user_id, 'User added!')

                    except:
                        calling(event.user_id)
                
                elif 'setNewCore' in request:
                    try:
                        users_using_coins.update({first: second})
                        write_msg(event.user_id, 'User {} added!'.format(first))
                    except:
                        print('chet ne to')


                elif '/givekCoin' in request: # ---> /givekCoin starrk 100000
                    # kvantorium_user{'starrk': '221396820'}
                    try:
                        kvantorium_users.update({ users_using_coins[first]: second })
                        print('cores - {}'.format(orange(cores)))
                        write_msg(event.user_id, 'coins to {} added! [given {} coins]'.format(first, second))
                    except:
                        write_msg(event.user_id, 'There is no user {}'.format(first))

                elif '/takekCoin' in request:
                    try:
                      if int(second) <= 0:
                          write_msg(event.user_id, "Che ti delaesh!!! chislo doljno bit' > 0 !!!!!!!!") 
                      # /takekCoin starrk 1000 -> {'starrk': id} -> {id: coins} 
                      print('Configuration =>> {} - {} = {}'.format(
                          int(kvantorium_users[users_using_coins[first]]), 
                          int(second),
                          int(kvantorium_users[users_using_coins[first]]) - int(second)
                      ))

                      
                      kvantorium_users[users_using_coins[first]] = int(kvantorium_users[users_using_coins[first]]) - 90 - int(second) 
                      print(info(kvantorium_users[users_using_coins[first]]))
                      write_msg(event.user_id, 'now User {} has {} coins'.format(first, kvantorium_users[users_using_coins[first]]))
                    except:
                      write_msg(event.user_id, 'Try it again ((')

                elif '/getAllUsers' in request:
                    stuff = ''

# users_using_coins = {}       # -> {'starrk': '22139620'}
# kvantorium_users  = {}       # -> {'221396820': '1000'} 

                    for k in users_using_coins:
                        # print('k = ', k)
                        # print('users_using_coins[k] = ', users_using_coins[k])
                        # print('kvantorium_users[users_using_coins[k]] = ', kvantorium_users[users_using_coins[k]])

                          information = '{} [vk.com/id{}] has {} coins'.format(k, 
                                    users_using_coins[k],
                                    kvantorium_users[users_using_coins[k]])

                          stuff += information + '\n'
                          write_msg(event.user_id, information)
                    write_msg(event.user_id, stuff)

                elif '/increaseEarning' in request:
                    # should set it in dictionary(database)
                    pass

                else:
                    calling(event.user_id)
    
            else:
                try:
                    first = request.split(' ')[1]
                except:
                    first = request

                if '/name' in request:
                    users_using_coins.update({first: event.user_id})
                    kvantorium_users.update({event.user_id: 0})
                    write_msg(event.user_id, 'You have been added to the database')
                    print('seom data => {}  '.format(green(kvantorium_users)))
                    print('some data => {}  '.format(orange(users_using_coins)))

                    # как создать счетчик который пополняет кредиты каждый день?

                elif '/getkCoin' in request:
                    #try:
                    write_msg(event.user_id, 'You have {} kCoins'.format((kvantorium_users[event.user_id])))
                    #except:
                    #    write_msg(event.user_id, 'I cant find you in database. kek... \ntry: /name <name> -> to create your account in own data')

                elif '/help' in request:
                    write_msg(event.user_id, "Ну, привет, мой дорогой Друг. Я так понял ты сюда пришел за kvantoCoin'нами?\nЛОВИ КОМАНДЫ В РЫЛО\n{}".format(information()))

                else:
                    calling_user(event.user_id)



