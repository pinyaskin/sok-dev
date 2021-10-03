from threading import Thread
import time

def first():
    for i in range(1,100):
        print('Запущено 1 ядро')
        time.sleep(0.5)

def second():
    for i in range(1,100):
        print('Запущено 2 ядро')
        time.sleep(0.3)
        if i == 20:
            thread3.start()

def third():
    for i in range(1,100):
        print('Запущено 3 ядро')
        time.sleep(1)

thread1 = Thread(target=first)
thread2 = Thread(target=second)
thread3 = Thread(target=third)


thread1.start()
thread2.start()
thread1.join()
thread2.join()