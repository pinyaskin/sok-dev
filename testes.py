# def test(x):
#     l = {
#         x == 2: '2',
#         x == 3: '3',
#         x == 4: 'Пошел ты'
#     }
#     return l[True]
# print(test(4))

# import sqlite3 as sq
#
# cur.fetchone()
#
#
# with sq.connect("places") as con:
#     cur = con.cursor()
#     cur.execute("")

# 2 часа = 7200 unix
# 10 минут = 600 unix

from datetime import datetime
import time
# import runpy

# print(time.time())
# a = datetime.strptime('20.12.2016 09:38:42,76', '%d.%m.%Y %H:%M:%S,%f')
# print(a.timestamp())
# bd = time.time()
# print(bd)
# print(datetime.fromtimestamp(bd))

# runpy.run_module(mod_name="test_lib")
# for i in range(1,100):
#     print(type(str(datetime.fromtimestamp(1629626492.17869).strftime('%H:%M:%S'))))
#     time.sleep(1)

# strftime('%Y-%m-%d %H:%M:%S')

# Документация архитектуры
# Питон каждые 2 минут проверяет статус времени последнего звонка. Если он составляет более двух часов, то
# начинается таймер, в течение 10-ти минут ждет звонка. Если звонок не поступает, поднимается тревога

import random

# def menu(smt):
#     cor = {
#         smt == 1: 'Меч',
#         smt == 2: 'Броня',
#         smt == 3: 'Сапоги',
#         smt == 4: 'Компьютер'
#     }
#     return cor[True]

def menu(smt):
    cor = {
        smt >= 1 and smt < 10: 'Меч',
        smt >= 10 and smt <= 15: 'Броня',
        smt > 15 and smt <= 85: 'Сапоги',
        smt > 85 and smt <= 100: 'Компьютер'
    }
    return cor[True]

def random_int():
    a = random.randint(1, 100)
    print(a, menu(a))

random_int()