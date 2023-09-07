def movieSerializer(raw_data):
    movies = []
    for movie in raw_data:
        movies.append(
            {
                'id': movie[0],
                'title': movie[1],
                'genre': movie[2],
                'release': movie[3],
                'rating': movie[4]
            }
        )
    return movies
