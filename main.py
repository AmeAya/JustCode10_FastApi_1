import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

# query = 'CREATE TABLE genres(id SERIAL PRIMARY KEY, title VARCHAR(50))'
# cursor.execute(query)
#
# query = 'CREATE TABLE movies(' \
#         'id SERIAL PRIMARY KEY,' \
#         'title VARCHAR(50),' \
#         'genre INTEGER,' \
#         'release INTEGER,' \
#         'rating REAL,' \
#         'FOREIGN KEY(genre) REFERENCES genres(id)' \
#         ')'
# cursor.execute(query)

# query = "INSERT INTO genres(title) VALUES('action');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('drama');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('horror');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('romance');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('comedy');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('adventure');"
# cursor.execute(query)
# query = "INSERT INTO genres(title) VALUES('thriller');"
# cursor.execute(query)
# connect.commit()

# query = "UPDATE genres SET id=7 WHERE title='action';"
# cursor.execute(query)
# query = "UPDATE genres SET id=1 WHERE title='drama';"
# cursor.execute(query)
# query = "UPDATE genres SET id=2 WHERE title='horror';"
# cursor.execute(query)
# query = "UPDATE genres SET id=3 WHERE title='romance';"
# cursor.execute(query)
# query = "UPDATE genres SET id=4 WHERE title='comedy';"
# cursor.execute(query)
# query = "UPDATE genres SET id=5 WHERE title='adventure';"
# cursor.execute(query)
# query = "UPDATE genres SET id=6 WHERE title='thriller';"
# cursor.execute(query)
# connect.commit()

# query = 'SELECT * FROM genres'
# cursor.execute(query)
# print(cursor.fetchall())

# with open('movies.sql', 'r') as file:
#     for insert in file.readlines():
#         insert = insert.replace('\n', '')
#         cursor.execute(insert)
# connect.commit()

# query = 'SELECT movies.id, movies.title, genres.title, movies.release, movies.rating FROM movies ' \
#         'JOIN genres ON movies.genre = genres.id'
# cursor.execute(query)
# print(cursor.fetchall())

cursor.close()
connect.close()
