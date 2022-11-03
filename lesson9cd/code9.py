import sqlite3

"""try:
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
    query = 'select sqlite_version();'
    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    cursor.close()
except sqlite3.error as error:
    print('Error occured - ', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Conection closed')
"""
#connection_obj = sqlite3.connect('sql.db')
#cursor_obj = connection_obj.cursor()
#cursor_obj.execute("DROP TABLE IF EXISTS Impact")

#table = """ CREATE TABLE Impact (
            #Email VARCHAR(255) NOT NULL,
            #First_Name CHAR(25) NOT NULL,
            #Last_Name CHAR(25));"""
#cursor_obj.execute(table)
#print("Table is Ready")
#connection_obj.close()

conn = sqlite3.connect('class.db')
cursor = conn.cursor()
table = """CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
#cursor.execute(table)
cursor.execute('''INSERT INTO STUDENT VALUES ('Ion', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Mihai', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Alex', '9th', 'C')''')
print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
update = cursor.execute("""UPDATE STUDENT SET CLASS = '10' WHERE NAME = 'Alex'""")
delete = cursor.execute("""DELETE FROM STUDENT WHERE NAME = 'ION'""")
result = cursor.execute("""SELECT * FROM STUDENT WHERE NAME = 'Alex'""")
print(result.fetchall())
conn.commit()