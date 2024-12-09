import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    # в not_telegram.db уже есть таблица Users, поэтому пусть называется Users_1(для модуля 14_5)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users_1(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
initiate_db()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users_1 (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    user = cursor.execute(f'SELECT username FROM Users_1').fetchall()
    connection.commit()
    for us in user:
        if us[0] == username:
            return True
    else:
        return False


# for i in range(1, 5):
#     cursor.execute(f'INSERT INTO Products(title, description, price) VALUES (?, ?, ?)', (f'Продукт {i}', f'Описани {i}', i*100))
# connection.commit()

def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    get_all = cursor.fetchall()
    return get_all
# print(get_all_products())


