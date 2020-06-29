# https://docs.python.org/3/library/sqlite3.html
import sqlite3

print(sqlite3.version)
print(sqlite3.version_info)
print(sqlite3.sqlite_version)
print(sqlite3.sqlite_version_info)

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()


##---------------------------------------------------------------
# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
