import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='naak' host ='localhost' port='5432'") # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='naak' host ='localhost' port='5432'") # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" %(item,quantity,price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

#insert("Water Glass", 10, 5)

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='naak' host ='localhost' port='5432'") # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("SELECT * from store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='naak' host ='localhost' port='5432'") # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='naak' host ='localhost' port='5432'") # Create connection to database, if no database then it will be created with this line of code
    cur = conn.cursor() # Create cursor object
    cur.execute("UPDATE store SET quantity =%s, price=%s WHERE item = %s",(quantity,price,item))
    conn.commit()
    conn.close()

#delete("Wine Glass")

#update(12,6,"Water Glass")
#print(view())

#create_table()
#insert("Orange",10,15)
delete("Orange")
print(view())