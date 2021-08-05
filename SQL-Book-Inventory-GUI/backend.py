import sqlite3

#### Connect ####
def connect():
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")

#### View All ####
def view_all():
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows

#### Add Entry ####
def add_entry(Title,Author,Year,ISBN):
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)",(Title,Author,Year,ISBN))
    conn.commit()
    conn.close()

#### To create Table ####
def create_table():
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

#### Update ####
def update(id,Title,Author,Year,ISBN):
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("UPDATE store SET Title =?, Author=?, Year=?, ISBN=? WHERE id =?",(Title,Author,Year,ISBN,id))
    conn.commit()
    conn.close()

#### To delete an item ####
def delete(id):
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("DELETE FROM store WHERE id=?",(id,))
    conn.commit()
    conn.close()

#### To search for an item ####
def search(Title="",Author="",Year="",ISBN=""):
    conn = sqlite3.connect('book.db') # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("SELECT * from store WHERE Title=? or Author = ? or Year = ? or ISBN = ?", (Title,Author,Year,ISBN))
    rows = cur.fetchall()
    conn.close()
    return rows

#create_table()





#delete(1610)
connect()
#add_entry('Colonialism','PK',1997,1610)
#add_entry('Colonialismal','PK',1997,1610)
#print(search(Author="PK"))
#print(search(Year=1997))

update(1, 'Colonialism', 'PKE', 19974444, 1610)
print(view_all())