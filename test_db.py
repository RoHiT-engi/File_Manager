# create a database or connect to one
import sqlite3

conn = sqlite3.connect('file_manager.db')
# create cursor
c = conn.cursor()

#c.execute("CREATE table work_file(login_ID varchar(10) primary key , last_working_directory varchar(40))")
'''c.execute("SELECT * FROM login")
record = c.fetchall()
print(record)'''

c.execute("INSERT OR IGNORE INTO login VALUES('admin1',12345678)")
#commit changes
conn.commit()
#close connection
conn.close()