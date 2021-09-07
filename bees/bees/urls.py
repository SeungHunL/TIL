from django.urls import path
from . import views
app_name = 'bees'
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('kill/<int:pk>',views.kill,name='kill'),
    path('update/<int:pk>',views.update,name='update'),
]

