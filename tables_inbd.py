import sqlite3

conn = sqlite3.connect('file_manager.db')
# create cursor
c = conn.cursor()

#c.execute("SELECT * FROM google_drive")
#c.execute("delete from google_drive")
#c.execute("SELECT * FROM work_file")
#c.execute("SELECT * FROM back_up")
#c.execute("SELECT * FROM login")
records = c.fetchall()
print(records)

#commit changes
conn.commit()
    #close connection
conn.close()
