import requests
import collections


search = "capital"

url = "http://movie_service.talkpython.fm/api/search/capital".format(search)

resp = requests.get(url)

resp.raise_for_status()

movie_data = resp.json()

movies = movie_data.get('hits')   
#print(resp.status_code)

print(type(movies),": \n",movies)
