import sqlite3 as sq

def create_db():
    con = sq.connect(database = r"wms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stock(name TEXT, appelation TEXT, domain TEXT, type TEXT, color TEXT, year INTEGER, location TEXT, quantity INTEGER, y_testing INTEGER)")
    con.commit()

create_db()
