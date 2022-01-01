

## 1.ORM에 대한 설명 중 틀린 것 2가지

1)객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Python -  SQL) 데이터를 변환하는 프로그래밍 기술

2)OOP프로그래밍에서  RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

3)Django는 내장 Python ORM을 사용함

4)SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성이 장점이다

```txt
1 Python -> Django
3 Python -> Django
```



## 2.CREATE에 사용되는 3가지 방법에 대한 코드 중 일부이다. 

## a,b,c에 들어갈 코드를 작성하시오

```txt
>>> article
<Article: Article object (None)>
>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>> <  a  >
>>> <  b  >
<QuerySet [Article: Article object (1)]>
>>> article = Article(title='second',content='django!!')
>>> <  a  >
>>> <  b  >
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
>>> Article.objects.<  c  >(title='third',content='django!')
<Article: Article object (3)>
```

```txt
a = article.save()
b = Article.objects.all()
c = create
```

## 3. 링크에 url을 직접 작성하는 것이 아니라 path() 함수의 name인자를 정의해서 사용하고 싶을 때 빈 칸에 들어갈 코드는?

```html
path('index/'), views.index, name='index'),
```

```
<a href="<-------->">메인 페이지</a>
```



```
{% url 'index' %}
```



