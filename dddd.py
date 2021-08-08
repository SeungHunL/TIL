import requests
from tmdb import TMDBHelper
from operator import itemgetter
 
def recon(title):
    th = TMDBHelper('key')
    movie_id = th.get_movie_id(title)
    url = th.get_request_url()
    
    requests.get(url)
    
def popular_count():
    tmdb_helper = TMDBHelper('057fb43d01b8fe3784d7f0c16bc470a1')
    url = tmdb_helper.get_request_url(region='KR',language='ko')
    data = requests.get(url).json()
    count = 0
    
    for i in data.get('results'):
        count += 1
    return count

def vote_average_movies():
    tmdb_helper = TMDBHelper('057fb43d01b8fe3784d7f0c16bc470a1')
    url = tmdb_helper.get_request_url(region='KR',language='ko')
    data = requests.get(url).json()
    
    list_8 = []
    for i in data['results']:
        if i['vote_average'] >= 8:
            list_8.append(i['title'])
    return list_8

def ranking():
    tmdb_helper = TMDBHelper('057fb43d01b8fe3784d7f0c16bc470a1')
    url = tmdb_helper.get_request_url(region='KR',language='ko')
    data = requests.get(url).json()
    list_5 = []
    
    newlist = sorted(data['results'], key=itemgetter('vote_average'), reverse=True)
    for i in range(0,4):
        list_5.append(newlist[i])
        
    return list_5
            
    
#print(popular_count())
#print(vote_average_movies())
print(ranking())
    