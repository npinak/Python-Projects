import sqlite3
from typing import ItemsView

def create_table():
    conn = sqlite3.connect('lite.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect('lite.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert("Water Glass", 10, 5)

def view():
    conn = sqlite3.connect('lite.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect('lite.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect('lite.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("UPDATE store SET quantity =?, price=? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close()

#delete("Wine Glass")

update(12,6,"Water Glass")
print(view())