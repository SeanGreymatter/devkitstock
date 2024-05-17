import sqlite3

con = sqlite3.connect('tutorial.db')
cur = con.cursor()

movie = input("Movie: ")
year = input("Year: ")
score = input("Score: ")
data = [(f"{movie}", year, score)]

cur.executemany("INSERT INTO movie VALUES (?, ?, ?)", data)

# cur.execute("CREATE TABLE movie(title, year, score)")

# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchone()

# cur.execute("""
# INSERT INTO movie VALUES
#             ('Monty Python and the Holy Grail', 1972, 8.2),
#             ('And Now for Something Completely Different', 1971, 7.5)
#             """)

# cur.execute("INSERT INTO movie VALUES ('Debbie Does Dallas', 1999, 10)")

# res = cur.execute("SELECT score FROM movie")
# print(res.fetchall())

con.commit()
con.close()