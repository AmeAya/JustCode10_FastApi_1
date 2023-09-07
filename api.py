from fastapi import FastAPI
from fastapi import Body
from fastapi.responses import JSONResponse
from serializers import movieSerializer
import sqlite3

app = FastAPI()


@app.get('/movies')
def getMovies(limit: int = -1):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    if limit == -1:
        query = 'SELECT movies.id, movies.title, genres.title, movies.release, movies.rating FROM movies ' \
                'JOIN genres ON movies.genre = genres.id'
    else:
        query = 'SELECT movies.id, movies.title, genres.title, movies.release, movies.rating FROM movies ' \
                'JOIN genres ON movies.genre = genres.id WHERE movies.id <= ' + str(limit)
    cursor.execute(query)
    movies = movieSerializer(cursor.fetchall())
    connect.close()
    connect.close()
    return JSONResponse(movies, status_code=200)


# HOMEWORK 5 September
@app.get('/genre')
def getGenreMovies(genre: str):
    # 127.0.0.1:8000/genre?genre=drama -> Возвращаем JSON с фильмами у которых жанр drama
    # 127.0.0.1:8000/genre?genre=action -> Возвращаем JSON с фильмами у которых жанр action
    # Challenge:
    # Сделать этот функционал в getMovies где genre будет необязательным параметром как limit.
    # То есть, если genre не передан, то вернуть фильмы всех жанров.
    # Если genre задан, то только фильмы этого жанра
    pass


@app.post('/release')
def getReleaseMovies(data=Body()):
    if 'release' in data.keys():
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        query = 'SELECT movies.id, movies.title, genres.title, movies.release, movies.rating FROM movies ' \
                'JOIN genres ON movies.genre = genres.id WHERE movies.release = ' + str(data['release'])
        cursor.execute(query)
        movies = movieSerializer(cursor.fetchall())
        connect.close()
        connect.close()
        return JSONResponse(movies, status_code=200)
    else:
        return JSONResponse({'msg': 'Release year is required'}, status_code=403)


@app.post('/movies')
def addNewMovie(data=Body()):
    required_fields = ['title', 'genre', 'release', 'rating']
    for field in required_fields:
        if field not in data.keys():
            return JSONResponse({'msg': field + ' is required'}, status_code=403)
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    query = "SELECT id FROM movies ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    movie_id = str(cursor.fetchone()[0] + 1)
    movie_title = data['title']
    movie_release = str(data['release'])
    movie_rating = str(data['rating'])
    query = "SELECT id FROM genres WHERE title='" + data['genre'] + "'"
    cursor.execute(query)
    movie_genre = cursor.fetchone()
    if movie_genre:  # Если коллекция(list, tuple, ...) не пуста, то ифка будет True
        movie_genre = movie_genre[0]
    else:
        query = "SELECT id FROM genres ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        movie_genre = str(cursor.fetchone()[0] + 1)
        query = "INSERT INTO genres(id, title) " \
                "VALUES(" + movie_genre + ", '" + data['genre'] + "')"
        cursor.execute(query)
        connect.commit()
    query = "INSERT INTO movies(id, title, genre, release, rating) " \
            "VALUES(" + movie_id + ", '" + movie_title + "', " + movie_genre + \
            ", " + movie_release + ", " + movie_rating + ")"
    cursor.execute(query)
    connect.commit()
    cursor.close()
    connect.close()
    return JSONResponse({'msg': 'Movie added successfully'}, status_code=200)


# HOMEWORK 7 September
# Создать ОТДЕЛЬНО в бд новую таблицу actors
# Данные для таблицы сгенерировать в mockaroo и отправить в таблицу
# Написать get функцию, которая возвращает список всех записей в этой таблице
# Написать post функцию, которая принимает данные для добавления новой записи в эту таблицу
