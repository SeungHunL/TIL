import articles
from django.shortcuts import render
# 명시적 상대경로
from .models import Article

# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # 1. 모든 게시물 조회
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html', context)

def new(request):
    return render(request,'articles/new.html')


def create(request):
    # new로 부터 title과 content를 받아서 저장
    title=request.GET.get('title')
    content=request.GET.get('content')
    # 1
    # article=Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 2
    article=Article(title=title, content=content)
    article.save()
    # 3 
    # Article.objects.create(title=title,content=conten)
    return render(request,'articles/create.html')
