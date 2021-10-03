import sqlite3 as sq
import time

status = 0
def status_update(caller,report):
    if int(report) == 1:
        stat = 'норма'
    else:
        stat = 'тревога'
    with sq.connect("ciro/db.sqlite3") as con:
        cur = con.cursor()
        cur.execute("UPDATE posts SET status = '"+stat+"' WHERE callerid == "+caller)
        cur.execute("UPDATE posts SET lastcall = '"+str(time.time()+18000)+"'WHERE callerid == "+caller)
        con.commit()