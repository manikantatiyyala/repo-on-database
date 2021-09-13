'''import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table lang (name, first_appeared)")

# This is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))

# The qmark style used with executemany():
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
    ("Java", 1972),
]
cur.executemany("insert into lang values (?, ?)", lang_list)

# And this is the named style:
cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
print(cur.fetchall())

con.close()'''

import sqlite3
con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE stock3
#               (date text, trans text, symbol text, qty real, price real)''')

#cur.execute('''DROP TABLE stock''')
#cur.execute('''DROP TABLE stocks''')



# Insert a row of data
#cur.execute("INSERT INTO stock3 VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#cur.execute("INSERT INTO stock3 VALUES ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)")
#cur.execute("INSERT INTO stock3 VALUES ('2006-04-06', 'SELL', 'IAM', 500, 53.0)")
#cur.execute("INSERT INTO stock3 VALUES ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)")



#Update records
#cur.execute("UPDATE stock3 SET price = 51.0 where symbol='IBM'")


#Delete records
cur.execute("DELETE from stock3 where price = 51.0")
print("total no.of records deleted :", con.total_changes)


# Save (commit) the changes
con.commit()
#print("Total number of rows updated :", con.total_changes)



#fetching and displaying records
for row in cur.execute('SELECT date,trans,symbol,price FROM stock3 ORDER BY price'):
    print("date = ", row[0])
    print("trans = ", row[1])
    print("symbol = ", row[2])
    print("price = ", row[3])


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()