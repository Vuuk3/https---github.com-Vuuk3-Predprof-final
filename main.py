from requests import get, post
import sqlite3

def create_db():
    con = sqlite3.connect('sqlite.db')
    cursor = con.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS test_table(
            date TEXT PRIMARY KEY,
            count INTEGER,
            rooms TEXT,
            result TEXT
        )
    '''
    cursor.execute('DROP TABLE IF EXISTS test_table;')
    cursor.execute(query)
    con.commit()
    con.close()

def write_db(date, count, rooms, result):
    rooms = list(map(str, rooms))
    rooms = ' '.join(rooms)
    con = sqlite3.connect('sqlite.db')
    cursor = con.cursor()
    query = f'''
        INSERT INTO test_table (date, count, rooms, result) VALUES ('{date}', {count}, '{rooms}', '{result}');
    '''
    cursor.execute(query)
    con.commit()
    con.close()


def build(windows_for_flat, windows):
    k = []
    ans = []
    y = len(windows)
    flat = 1
    e = 0
    rooms = []
    for i in range(y): # Перебор по кол-ву этажей
        for j in windows_for_flat: # Перебор по этажу
            for m in range(j):
                floor = f'floor_{i + 1}'
                k.append((flat, windows[floor][e])) # Запись номера комнаты и состояния окна
                if windows[floor][e] and flat not in rooms: # Подготовка кол-ва комнат и номеров комнат для ответа
                    rooms.append(flat)
                e += 1
            flat += 1
        ans.insert(0, k) # Добавление в начало списка
        k = []
        e = 0
    return ans, len(rooms), rooms


def get_one_data(date):
    url = 'https://olimp.miet.ru/ppo_it_final'
    day, month, year = date[0], date[1], date[2] # Получение дня, месяца, года
    # Получение данных зва один день
    data = get(url + f'?day={day}&month={month}&year={year}', headers={'X-Auth-Token': 'ppo_11_10974'}).json()['message']
    windows_for_flat = data['windows_for_flat']['data'] # Количество окон для каждого этажа в формате [3, 2, 1]
    windows = data['windows']['data'] # Словарь, где ключ - этаж, а значение - список состояний окон
    return build(windows_for_flat, windows)


def get_data(mode=0):
    url = 'https://olimp.miet.ru/ppo_it_final'
    message = get(url + '/date', headers={'X-Auth-Token': 'ppo_11_10974'}).json()['message'] # Получение дат
    answers = []
    for i in message:
        date = i.split('-')
        ans, c, rooms = get_one_data(date)
        result = post_data(i, c, rooms)
        if mode == 2:
            answers.append((result, c, rooms))
        else:
            answers.append((result, ans))
        if mode == 1:
            write_db(i, c, rooms, result)
    return answers

def post_data(date, count, rooms): # Проверка на правильность
    url = 'https://olimp.miet.ru/ppo_it_final'
    data = {
        "data": {
            "count": count,
            "rooms": rooms
        },
        "date": date
    }
    return post(url, json=data, headers={'X-Auth-Token': 'ppo_11_10974', 'Content-Type': 'application/json'}).json()['message']


create_db()
def n2():
    for i in (get_one_data(['25', '01', '23'])[0]):
        print(i)


def n3():
    for i in get_data():
        for j in i[-1]:
            print(j)
        print()

def n6():
    for i in get_data(mode=2):
        print(i)
        print()

def n7(s):
    for i in (get_one_data(s.split('-'))[0]):
        print(i)

def n8():
    for i in get_data(mode=2):
        for j in i[-1]:
            print(j)
        print()

n2()
n3()
n6()
n7(input)
n8()
