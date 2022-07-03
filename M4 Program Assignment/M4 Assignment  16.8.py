import sqlalchemy as sa
import sqlite3 as s3

conn = sa.create_engine(
    'sqlite:////Users/isaia/Desktop/Ivy Tech/Homework - SDEV220/M4/books.db')

# Commented out to prevent errors for tables already being created or values repeating.
# conn.execute(
#     '''CREATE TABLE books(title VARCHAR(40), author VARCHAR(30), year INT) ''')

# ins = 'INSERT INTO books (title, author, year) VALUES (?,?,?)'
# conn.execute(
#     'INSERT INTO books VALUES ("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
# conn.execute(
#     'INSERT INTO books VALUES ("Perdido Street Station", "China Miéville", 2000)')
# conn.execute(
#     'INSERT INTO books VALUES ("The Spellman Files", "Lisa Lutz", 1992)')
# conn.execute('INSERT INTO books VALUES ("Small Gods", "Terry Pratchett", 2007)')
# conn.execute('INSERT INTO books VALUES ("Thud!", "Terry Pratchett", 2005)')

rows = conn.execute('SELECT title FROM books ORDER BY title ASC')

for row in rows:
    print(row)


# cn = s3.connect('books.db')

# curs = cn.cursor()
# curs.execute(
#     '''CREATE TABLE books(title VARCHAR(40), author VARCHAR(30), year INT) ''')


# curs.execute(
#     'INSERT INTO books VALUES ("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
# curs.execute(
#     'INSERT INTO books VALUES ("Perdido Street Station", "China Miéville", 2000)')
# curs.execute(
#     'INSERT INTO books VALUES ("The Spellman Files", "Lisa Lutz", 1992)')
# curs.execute('INSERT INTO books VALUES ("Small Gods", "Terry Pratchett", 2007)')
# curs.execute('INSERT INTO books VALUES ("Thud!", "Terry Pratchett", 2005)')
