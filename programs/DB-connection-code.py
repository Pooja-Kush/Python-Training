import mysql.connector

myDB = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_DB"
)

# print(myDB)

myCursor = myDB.cursor()

# myCursor.execute("CREATE DATABASE python_DB")


myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)


# myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# myCursor.execute("SHOW TABLES")
#
# for x in myCursor:
#     print(x)


# myCursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Low street 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Side way 1633')
# ]
#
# myCursor.executemany(sql, val)
#
# myDB.commit()
#
# print(myCursor.rowcount, "was inserted.")


# myCursor.execute("SELECT * FROM customers WHERE id='1'")
#
# myResult = myCursor.fetchall()
#
# for x in myResult:
#     print(x)
    # print("Name : ", x[0], " || Address : ", x[1])
