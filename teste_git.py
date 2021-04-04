#teste git
import os
import mysql.connector as mysql
from getpass import getpass
from mysql.connector import Error

def testString():
    print('teste strings...')
    name = 'Daniel'
    age = 36
    str = 'Meu nome é {} e eu tenho {}'
    print(str.format(name,age))


def mysqlCon():
    print('iniciando coleta MySQL...')
    try:
        with mysql.connect(
                            host="localhost",
                            user="root",
                            password="xgq984dgf",
                            database="Base_Teste",
                            auth_plugin="mysql_native_password") as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM Cliente")
            for myresult in mycursor.fetchall():
                print(myresult)
    except Error as e:
        print(e)

def main():
    mysqlCon()

if __name__ == "__main__":
    main()    

