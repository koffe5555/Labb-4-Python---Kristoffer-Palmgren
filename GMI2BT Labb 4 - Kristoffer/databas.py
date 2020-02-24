import sqlite3

con = sqlite3.connect('data.db')
c = con.cursor()

c.execute("""CREATE TABLE rng(
    first text,
    second text,
    third text
    )""")

con.commit()
con.close()