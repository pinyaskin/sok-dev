import time
import sqlite3 as sq

def check_time():
    while 1:
        with sq.connect("ciro/db.sqlite3") as con:
            cur = con.cursor()
            new = cur.execute("SELECT callerid,lastcall FROM posts")
            warn_obj = []
            for values in new:
                caller = str(values[0])
                last = float(values[1] or 0)
                now = time.time()+18000
                if type(last) == float:
                    dif = now - last
                    if dif >= 7260:
                        warn_obj.append(caller)
            for caller_list in warn_obj:
                cur.execute("UPDATE posts SET status = 'тревога' WHERE callerid ==" + caller_list)
        time.sleep(600)