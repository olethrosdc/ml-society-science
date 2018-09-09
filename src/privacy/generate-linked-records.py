import sqlite3
conn = sqlite3.connect('financial.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE 
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('Name','ID','Account',100,35.14)")
# Larger example that inserts many records at a time
purchases = [('Antonio Banderas, '12209713', 'q')]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
