import requests

URL = 'https://open123movies.com/tvshow/legacies-3b4zBOxL/this-year-will-be-different-qgJg92zL/vydVQgqn/watch-free.html'
page = requests.get(URL)
pprint(page)
