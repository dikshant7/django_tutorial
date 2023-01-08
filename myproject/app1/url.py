from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),#root url where views.index means the function performed when you open this url and index is the name of this url
    # path('download',views.index,name=index)// for download url
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout ,name='logout'),
    path('post/<str:pk>',views.post ,name='post') #where pk is variable of type string
]