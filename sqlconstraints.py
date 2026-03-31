import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_10 (SNO INTEGER PRIMARY KEY,
             ROLL_NO INTEGER NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT DEFAULT(15),
             GENDER CHAR(1) NOT NULL,
             EMAIL TEXT NOT NULL,
             CONTACT_NO REAL NOT NULL);''')

print("Table created successfully")

conn.execute('''INSERT INTO CLASS_10(SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL,CONTACT_NO)VALUES
             (101,1,"Aarya",15,"F","aarya98@gmail.com",9437891234),
             (102,2,"Mahi",15,"F","mahi009@gmail.com",8176534587),
             (103,3,"Abhishek",15,"M","abhi45@gmail.com",7891239765),
             (104,4,"Rakesh",15,"M","rakesh345@gmail.com",8123498766);''')

conn.commit()
print("Records created successfully")

tables = pd.read_sql("""SELECT * FROM CLASS_10;""",conn)
print(tables)
