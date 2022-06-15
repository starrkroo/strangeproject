#!/usr/bin/env python3


import sqlite3
from os import getcwd

class Working:
    def __init__ (self):
        connect = sqlite3.connect(path_to_db)
        cursor = connect.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Work(id INTEGER PRIMARY KEY AUTOINCREMENT, core VARCHAR(20), core_id VARCHAR(12))')
        query = """INSERT INTO Work(core, core_id) VALUES(?, ?)"""
        cursor.execute(query, ("starrk", "221396820",))

    def starting(self):
        global connect, cursor
        connect = sqlite3.connect(path_to_db)
        cursor = connect.cursor()
    
    def pushing(self, core = False, core_id = False, error = False):
        self.starting()
        cursor.execute('CREATE TABLE IF NOT EXISTS Work(id INTEGER PRIMARY KEY AUTOINCREMENT, core VARCHAR(20), core_id VARCHAR(12))')
        query = """INSERT INTO Work(core, core_id) VALUES(?, ?)"""
        if error:
            raise Exception('User alredy created')
        if not len(str(core_id)):
            print("Input ID!!!!!!!")
            return;
        if not len(str(core)):
            print("Input NAME!!!!!!")
            return ;

        try:
            for k in self.get_data:
                if str(core) == str(k[1]) or str(core) == str(k[2]):
                    self.pushing(error = True)
        except:
            pass

        cursor.executemany(query, [(core, core_id)])
        connect.commit()
        cursor.close(); connect.close()

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
 
    # def update_dataBase(self, first_name = False, swap_name = False):

    #     connect = sqlite3.connect(path_to_db)
    #     cursor = connect.cursor()

    #     if swap_name and (swap_name != ''):
    #         for k in self.get_data:
    #             print('{} == {} => {}'.format(str(swap_name), str(k[0]), str(swap_name) == str(k[0])))
    #             if ( str(swap_name) == str(k[0]) ):
    #                 raise Exception('User alredy have same name..\n try it again');
    #         cursor.execute('UPDATE Work SET core = ? WHERE core = ?', (str(swap_name), str(first_name)))
    #         connect.commit()
    #         cursor.close(); connect.close()
    #         return;


    def delete_data(self, name = False, id = False, isAll = False): # if name has value -> name = <value>

        connect = sqlite3.connect(path_to_db)
        cursor = connect.cursor()

        if isAll and isAll != '':
            for k in self.get_data():
                cursor.execute('DELETE FROM Work WHERE name = ?', (k[1],))

        if name and (name != ''):
            for k in self.get_data:
                #print('{} in {} = {}'.format(name, k, name in k))
                if name == k[1]:
                    cursor.execute('DELETE FROM Work WHERE core = ?', (name,))
        elif id and (id != ''):
            for k in self.get_data:
                #print('{} == {} = {}'.format(id, k[1], id == k[1]))
                if id == k[2]:
                    cursor.execute('DELETE FROM Work WHERE core_id = ?', (id,))

    
        connect.commit()
        cursor.close()
        connect.close()

    @property
    def get_data(self):
        connect = sqlite3.connect(path_to_db)
        cursor = connect.cursor()
        try:
            cursor.execute("SELECT * FROM Work")
            return cursor.fetchall()
        except:
            pass


    @property
    def drop_dataBase(self):
        connect = sqlite3.connect(path_to_db)
        cursor = connect.cursor()
        try:
            cursor.execute("DROP TABLE Work")
            connect.commit()
        except:
            print("already deleted")



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

def deleting():
    item.drop_dataBase

def appending():
    name1 = input('Cores name: ')
    core_id = input('Cores id: ')

    try:
        item.pushing(name1, core_id)
    except Exception as e: # means that there is same queryes
        print('try it again\n\t{}'.format(e))

def updating():
    first_name1 = input("Enter name: ")
    swap_name1 = input("Enter name which u want to swap: ")
    try:
        item.update_dataBase(first_name1, swap_name1)
    except Exception as e:
        print('Error: {}'.format(e))

def delete_data1():
    name = input('Cores name: ')
    id = str(input('Cores id: '))
    if name == 'all' or id == 'all':
      item.delete_data(isAll = True)
      return 

    item.delete_data(name, id)    

def drop_dataBase():
    item.drop_dataBase

if __name__ == '__main__':
    path_to_db = 'data.db'
    item = Working()
    run = True
    while run:
        choice = input("[S]how or [A]ppend or [R]emove or [D]ropDataBase or [E]xit: \n")
        if choice in ['E', 'e']:
            run = False
        elif choice in ['S', 's']:
            showing()
        elif choice in ['A', 'a']:
            appending()
        elif choice in ['U', 'u']:
            updating()
        elif choice in ['D', 'd']:
            drop_dataBase()
        elif choice in ['R', 'r']:
            delete_data1()

else:
    path_to_db = '{}/Logs/cores/data.db'.format(getcwd())
