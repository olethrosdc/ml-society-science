import sqlite3
conn = sqlite3.connect('example.db')

# get a reference to the data
c = conn.cursor()

# Add Some New Records
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# fetch data
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# get the average price for IBM
c.execute('SELECT AVG(price) FROM stocks WHERE symbol="IBM"')
c.fetchall()



