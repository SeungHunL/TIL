from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.


# 전체 영화 목록 조회
def index(request):
    movies = Movie.objects.all()
    
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

# 새로운 영화 작성 form 
def new(request):
    return render(request,'movies/new.html')

# 사용자가 제출한 데이터를 새로운 movie에 저장
def create(request):
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.poster_path = request.POST.get('poster_path')
    movie.overview = request.POST.get('overview')
    movie.save()
    return redirect('movies:detail',movie.pk)

# 단일 영화 상세 조회
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request,'movies/detail.html',context)


def update(request,pk):
    movie = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.poster_path = request.POST.get('poster_path')
    movie.overview = request.POST.get('overview')
    movie.save()

    return redirect('movies:detail', movie.pk)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def edit(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)
