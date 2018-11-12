import requests
import collections

MovieResult = collections.namedtuple(
    "MovieResults",
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres",
)

search = 'runner'

url = "http://movie_service.talkpython.fm/api/search/{}".format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get("hits")

# movies = []
# for md in movies_list:
#     m = MovieResult(
#         imdb_code=md.get("imdb_code"),
#         title=md.get("title"),
#         duration=md.get("duration"),
#         director=md.get("director"),
#         year=md.get("year", 0),
#         rating=md.get("rating", 0),
#         imdb_score=md.get("imdb_score", 0.0),
#         keywords=md.get("keywords"),
#         genres=md.get("genres")
#     )
#     movies.append(m)

def method(x,y,z):
    pass


def method(7,2,z=2)


movies = []
for md in movies_list:
    m = MovieResult(
        imdb_code=md.get("imdb_code"),
        title=md.get("title"),
        duration=md.get("duration"),
        director=md.get("director"),
        year=md.get("year", 0),
        rating=md.get("rating", 0),
        imdb_score=md.get("imdb_score", 0.0),
        keywords=md.get("keywords"),
        genres=md.get("genres")
    )
    movies.append(m) 

print("Found {} movies from search {}".format(len(movies), search))

for m in movies:
    print("{}  -----  {}".format(m.year, m.title))
