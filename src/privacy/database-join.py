import sqlite3
conn = sqlite3.connect('drugs.db')

# get a reference to the data
c = conn.cursor()

c.execute('''CREATE TABLE drugs
             (birth text, zip text, drugs text)''')

# Add Some New Records
purchases = [('1996-03-28', '1123', 'yes'),
             ('1998-12-01', '1493', 'no'),
             ('1995-05-05', '2131', 'yes'),
             ('1999-11-08', '2931', 'no'),
             ('1985-11-08', '1014', 'no'),
             ('1988-05-07', '1491', 'yes'),
             ('1989-10-01', '2238', 'no'),
             ('1988-09-03', '2313', 'yes'),
            ]

c.executemany('INSERT INTO drugs VALUES (?,?,?)', purchases)

c.execute('''CREATE TABLE registration
             (birth text, zip text, name text)''')

voter = [('1996-03-28', '1123', 'John Doe'),
         ('1928-12-01', '1493', 'James Madisson'),
        ('1935-05-05', '2131', 'Pu Li'),
         ('1949-11-08', '2931', 'Goran Glikovits'),
         ('1945-11-08', '1014', 'Natalia Glakova'),
         ('1968-05-07', '1491', 'Mady Madisson'),
        ('1979-10-01', '2238', 'Lia Johnsson'),
         ('1978-09-03', '2313', 'Yama Tanaka'),
]



c.executemany('INSERT INTO registration VALUES (?,?,?)', voter)

c.execute('SELECT * FROM drugs JOIN registration ON drugs.birth = registration.birth')

print(c.fetchall())




