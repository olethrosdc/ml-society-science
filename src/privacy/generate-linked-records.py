import sqlite3
conn = sqlite3.connect('financial.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE finance
             (name text, id text, zip text, town text, age int, credit int, debit int)''')

# Insert a row of data
clients = [('Antonio Banderas', '12209713', '2387', 'Goteborg', 60, 100, 200),
             ('Jim Lee', '3249872341', '1237', 'Malmo', 49, 500, 1000),
             ('Nwein Asci', '012851237', '1323', 'Orebro', 110, 293848, 987234),
             ('Meow Kittie', '98127312', '3233', 'Klmron', 39, 293848, 987234),
             ('Joanna Batiste', '98749801', '2387', 'Goteborg', 40, 100, 200),
             ('Emilia Lansheim', '8714112', '1237', 'Malmo', 59, 500, 1000),
             ('Silvia Rosalicci', '932496234', '1323', 'Orebro', 20, 293848, 987234),
             ('Lisa Rothkopf', '89712892', '3233', 'Klmron', 89, 293848, 987234),
]

c.execute('''CREATE TABLE census
             (name text, id text, zip text, town text, age int, sex text, party text)''')
# Insert a row of data
voters = [('Antonio Banderas', '12209713', '2387', 'Goteborg', 'm', 'nazi'),
             ('Jim Lee', '3249872341', '1237', 'Malmo', 'm', 'communist'),
             ('Nwein Asci', '012851237', '1323', 'Orebro', 'm', 'socialist'),
             ('Meow Kittie', '98127312', '3233', 'Klmron', 'm', 'green'),
             ('Joanna Batiste', '98749801', '2387', 'Goteborg', 'f', 'capitalist'),
             ('Emilia Lansheim', '8714112', '1237', 'Malmo', 'f', 'communist'),
             ('Silvia Rosalicci', '932496234', '1323', 'Orebro', 'f', 'socialist'),
             ('Lisa Rothkopf', '89712892', '3233', 'Klmron', 'f', 'green'),
]



c.executemany('INSERT INTO finance VALUES (?,?,?,?,?,?,?)', clients)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
