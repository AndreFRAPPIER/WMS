import sqlite3 as sq

def create_tab_wine():
    con = sq.connect(database = r"wms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stock(name TEXT, appelation TEXT, domain TEXT, type TEXT, color TEXT, year INTEGER, location TEXT, quantity INTEGER, y_testing INTEGER, id_lot INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

def create_tab_alcool():
    con = sq.connect(database = r"wms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS alcool(name TEXT, marque TEXT, age INT, quantite INT, id_lot INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

# if __name__ == "__main__":
#     create_tab_wine()
