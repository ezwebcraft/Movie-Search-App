import requests
import collections

MovieResult = collections.namedtuple(
    "MovieResults",
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

def find_movies(search_text):

    search = input("Enter a name of a movie: ")

    url = "http://movie_service.talkpython.fm/api/search/{}".format(search)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get("hits")

    movies = [MovieResult(**md) for md in movies_list]

    movies.sort(key=lambda m: -m.year)

    return movies

