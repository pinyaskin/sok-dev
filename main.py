import asyncio
import panoramisk
from panoramisk import Manager
from threading import Thread
import dbscript
import timer as tm

manager = Manager(loop=asyncio.get_event_loop(),
                  host='127.0.0.1',
                  port='5038',
                  username='testuser',
                  secret='12345678',
                  ping_delay='5'
                  )



async def callback(mngr: panoramisk.Manager, msg: panoramisk.message) -> None:
    if msg.event == 'FullyBooted':
        print('Connection Ok, Privilege:', msg.Privilege)
    elif msg.event == 'Registry':
        print(f'Trunk status is {msg.Status}')
    elif msg.event == 'ChallengeSent':
        print(msg.AccountID, 'is trying to connect with', msg.Service)
    elif msg.event == 'Newchannel':
        print(msg.Channel, 'is calling to', msg.Exten)
    elif msg.event == 'DialEnd' and msg.DialStatus == 'ANSWER':
        print(msg.Exten, 'answered to', msg.CallerIDNum)
    elif msg.event == 'DialEnd' and msg.DialStatus == 'BUSY':
        print(msg.Exten, 'is busy for', msg.CallerIDNum)
    # elif msg.event == 'DTMFEnd':
    #     print(msg.CallerIDNum,'pressed', msg.Digit)
    #     report(msg.CallerIDNum,msg.Digit)
    elif msg.event == 'Newexten' and msg.Context == 'warning':  # передаем тревогу в бд
        print('Номер', msg.CallerIDNum, 'сообщил', msg.Context)
        report(msg.CallerIDNum, msg.Context)
    elif msg.event == 'Newexten' and msg.Context == 'normal':  # передаем норму в бд
        print('Номер', msg.CallerIDNum, 'сообщил', msg.Context)
        report(msg.CallerIDNum, msg.Context)
    elif msg.event == 'Hangup':
        print(msg.CallerIDNum, 'call ended')


def report(callid, reportmsg):
    if reportmsg == 'normal':
        dbscript.status_update(callid, 1)
    elif reportmsg == 'warning':
        dbscript.status_update(callid, 2)


def main(mngr: panoramisk.Manager) -> None:
    mngr.register_event('*', callback=callback)
    mngr.connect()

    try:
        mngr.loop.run_forever()
    except (SystemExit, KeyboardInterrupt):
        mngr.loop.close()
        exit(0)


if __name__ == '__main__':
    check_thread1 = Thread(target=main, args=(manager,))
    timer_thread2 = Thread(target=tm.check_time)
    check_thread1.start()
    timer_thread2.start()
    check_thread1.join()
    timer_thread2.join()