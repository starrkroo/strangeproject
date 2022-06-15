#!/usr/bin/env python3

import mysql.connector
from os import getcwd

class Working:
    
    def starting(self):
        global connect, cursor
        connect = mysql.connector.connect(
            host = 'remotemysql.com', 
            user ='dAEwLGf27F', 
            password ='rnfA4rQCxA', 
            database = 'dAEwLGf27F')
        cursor = conn.cursor(buffered=True)
    
    def pushing(self, name = False, user_id = False, user_coins = False, increaseEarning = False, error = False):
        self.starting()
        cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Work(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                vk_id INTEGER
                first_name VARCHAR(50), 
                last_name VARCHAR(50), 
                coin INTEGER,
                clicks INT,
                is_admin INTEGER,
                is_prepod INTEGER,
                is_core INTEGER,
                code_invate INTEGER,
                user_ip TEXT,
                reg INTEGER
                )''')
        query = """INSERT INTO Work(name, user_id, name_coins, increaseEarning) VALUES(s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s))"""
        if error:
            raise Exception('User alredy created')
        if not len(str(user_id)):
            print("Input ID!!!!!!!")
            return;
        if not len(str(name)):
            print("Input NAME!!!!!!")
            return;

        try:
            for k in item.get_data():
                if str(name) == str(k[1]) or str(user_id) == str(k[2]):
                    self.pushing(error = True)
        except TypeError:
            print("Got a typeError error")！"!!"
            
        if user_coins and user_coins != '':  
            try:
                user_coins = int(user_coins)
            except:
                raise Exception('Why user_coins - str?\n should be int')
        else: user_coins = 0
        if increaseEarning and increaseEarning != '':
            try:
                increaseEarning = int(increaseEarning)
            except:
                raise Exception('Why increaseEarning - str?\nshould be int')
        else: increaseEarning = 10
        cursor.execute(query, (name, user_id, user_coins, increaseEarning, )) # 221396820
        connect.commit()
        cursor.close(); connect.close()

    def drop_dataBase(self):
        connect = mysql.connector.connect(
            host = 'remotemysql.com', 
            user ='dAEwLGf27F', 
            password ='rnfA4rQCxA', 
            database = 'dAEwLGf27F')
        cursor = conn.cursor(buffered=True)
        try:
            cursor.execute("DROP TABLE Work")
            connect.commit()
        except:
            print("already deleted")


    def outputing(self, name = False, user_id = False):
        self.starting()
        try:
            cursor.execute("SELECT * FROM Work")
        except Exception as e:
            return e
        sht = cursor.fetchall()
        cursor.close(); connect.close()
        for index, item in enumerate(sht):
            if name == 'all':
                # list  
                return sht
            else: 
                if name in item:
                    # tuple
                    return sht[index]
    
    def isUserCreated(self, name, user_id):
        try:
            # try to check that user not here
            for k in self.get_data():
                if str(name) == str(k[1]) and str(user_id) == str(k[2]):
                    return True
        except TypeError as e:
            print("Got a TypeError => \nError: {}".format(e))
    
    def get_increase(self, user):
      if user and (user != ''):
        for k in self.get_data():
          if str(k[1]) == str(user):
            return k[4]
        raise Exception("There is no user <{}>".format(user))
      

        

    def update_dataBase(self, first_name, swap_name = False, kCoins = False, increaseEarning = False, everyDay = False):
        # print('Datas: \n\tfirst_name = {}\n\tswap_name = {}'.format(first_name, swap_name))

        connect = mysql.connector.connect(
            host = 'remotemysql.com', 
            user ='dAEwLGf27F', 
            password ='rnfA4rQCxA', 
            database = 'dAEwLGf27F')
        cursor = conn.cursor(buffered=True)

        if swap_name and (swap_name != ''):
            for k in self.get_data():
                #print('{} == {} => {}'.format(str(swap_name), str(k[0]), str(swap_name) == str(k[0])))
                if ( str(swap_name) == str(k[1]) ):
                    raise Exception('User alredy have same name..<{}>\n try it again'.format(swap_name));
            cursor.execute('UPDATE Work SET name = ? WHERE name = ?', (str(swap_name), str(first_name)))
            connect.commit()
            cursor.close(); connect.close()
            return;

        elif kCoins and (kCoins != ''):
            try: isRunning = isinstance(int(kCoins), int)
            except: raise Exception("You are working not with integer..")
            #if (kCoins).split('.')[0].isdigit():
            if isRunning:
                for index, k in enumerate(self.get_data()):
                    try:
                        if first_name in k[2]:
                            if everyDay:
                                cursor.execute('UPDATE Work SET name_coins = ? WHERE user_id = ?', ((kCoins), first_name)); connect.commit()
                            else:
                                cursor.execute('UPDATE Work SET name_coins = ? WHERE user_id = ?', (str(int(self.get_data()[index][3]) + int(kCoins)), first_name)); connect.commit()
                            return (str(int(self.get_data()[index][3])))
                    except TypeError:
                        raise Exception('You should correctly write name')

        elif increaseEarning and increaseEarning != '':
            try: isRunning = isinstance(int(increaseEarning), int)
            except: raise Exception('Your are working not with integer..')
            if isRunning:
                for index, k in enumerate(self.get_data()):
                    if first_name in k[1]:
                        cursor.execute('UPDATE Work SET increaseEarning = ? WHERE name = ?', (str(int(self.get_data()[index][4]) + int(increaseEarning)), first_name)); connect.commit()
                        return (str(int(self.get_data()[index][3])))

    def delete_data(self, name = False, id = False, isAll = False):

        connect = mysql.connector.connect(
            host = 'remotemysql.com', 
            user ='dAEwLGf27F', 
            password ='rnfA4rQCxA', 
            database = 'dAEwLGf27F')
        cursor = conn.cursor(buffered=True)

        if isAll and isAll != '':
            for k in self.get_data():
                cursor.execute('DELETE FROM Work WHERE name = ?', (k[1],))

        if name and (name != ''):
            for k in self.get_data():
                #print('{} in {} = {}'.format(name, k, name in k))
                if name == k[1]:
                    cursor.execute('DELETE FROM Work WHERE name = ?', (name,))
        elif id and (id != ''):
            for k in self.get_data():
                #print('{} == {} = {}'.format(id, k[1], id == k[1]))
                if id == k[2]:
                    cursor.execute('DELETE FROM Work WHERE user_id = ?', (id,))
    
        connect.commit()
        cursor.close()
        connect.close()

    def get_data(self, name = False, user_id = False):
        connect = mysql.connector.connect(
            host = 'remotemysql.com', 
            user ='dAEwLGf27F', 
            password ='rnfA4rQCxA', 
            database = 'dAEwLGf27F')
        cursor = conn.cursor(buffered=True)
        try:
            cursor.execute("SELECT * FROM Work")
            return cursor.fetchall()
        except:
            if (name and name != '') and (user_id and user_id != ''):
              self.pushing(name, user_id)
            else:
              raise Exception("there is no database..") from None



item = Working()
def showing():
    name = input("Your query(can be id) : ")
    if name.isdigit():
        new_data = item.outputing(user_id = name)
    new_data = item.outputing(name = name)

    if isinstance(new_data, list): 
        for k in new_data: 
            print(k)
    elif isinstance(new_data, tuple): 
        print(new_data)

def appending():
    name1 = input('User name: ')
    user_id = input("User id: ")
    how_many_coins = input("How many coins(enter): ")
    increaseEarning = input("How many kCoins per day(enter): ")

    try:
        item.pushing(name1, user_id, how_many_coins, increaseEarning)
    except Exception as e:
        print("try it again\n\t{}".format(e))

def delete_data():
    name1 = input('User name: ')
    id = str(input('User id: '))

    if name1 == 'all' or id == 'all':
        item.delete_data(isAll = True)
        return 

    item.delete_data(name1, id)

def updating():
    first_name1 = input("Enter name: ")
    kCoins = input("How many coins \n<You can pass this>\n\t: ")
    swap_name1 = input("Enter name which u want to swap: ")
    increaseEarning = input("Enter count of increaseEarning: ")
    try:
        item.update_dataBase(first_name1, swap_name1, kCoins, increaseEarning)
    except Exception as e:
        print('Error: {}'.format(e))

def checking1():
    name = input("Name: ")
    print(item.isUserCreated(name))

def drop_database():
    item.drop_dataBase()

if __name__ == '__main__':
    path_to_db = 'data.db'
    run = True
    while run:
        choice = input("[S]how or [A]ppend or [R]emove or [U]pdate or [C]heck or [D]ropDatabase or [E]xit: \n")
        if choice in ['E', 'e']:
            run = False
        elif choice in ['S', 's']:
            showing()
        elif choice in ['A', 'a']:
            appending()
        elif choice in ['U', 'u']:
            updating()
        elif choice in ['C', 'c']:
            checking1()
        elif choice in ['D', 'd']:
            drop_database()
        elif choice in ['R', 'r']:
            delete_data()

else:
    #path_to_db = 'data.db'
    path_to_db = '{}/Logs/users/data.db'.format(getcwd())
