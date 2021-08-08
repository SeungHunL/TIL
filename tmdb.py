import requests
from pprint import pprint
class TMDBHelper:
    
    def __init__(self,api_key=None):
        self.api_key = api_key
        
    def get_request_url(self,method='/movie/popular',**kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'
        
        for k,v in kwargs.items():
            request_url += f'&{k}={v}'
            
        return request_url
    
    #제목으로 영화 검색 후, 검색결과에서 id를 찾아서 return
    def get_movie_id(self, title):
        request_url = self.get_request_url('/search/movie',query=title, language='ko', region='KR')    
        data = requests.get(request_url).json()
        
        pprint(data)
        
        results = data['results']
        if results:
            movie_id = results[0]['id']
            return movie_id
        else:
            return None
            
        movie = data['results'][0]
        
        return movie['id']
    
#tmdb_helper = TMDBHelper('057fb43d01b8fe3784d7f0c16bc470a1')        
#tmdb_helper.get_request_url(language='ko', region='KR')
#print(tmdb_helper.get_movie_id('충생기'))


'''
url =  'https://api.themoviedb.org/3/movie/550?api_key=057fb43d01b8fe3784d7f0c16bc470a1'

https://api.themoviedb.org/3/movie/550
?
api_key=057fb43d01b8fe3784d7f0c16bc470a1
&
language=ko
&
region=KR

https://api.themoviedb.org/3/movie/popular?api_key=057fb43d01b8fe3784d7f0c16bc470a1&language=ko&region=KR

https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Jack+Reacher


https://api.themoviedb.org/3
/movie/75780/recommendations
?
api_key=057fb43d01b8fe3784d7f0c16bc470a1
&language=ko
&page=1

https://api.themoviedb.org/3
/movie/75780/credits
api_key=057fb43d01b8fe3784d7f0c16bc470a1

'''