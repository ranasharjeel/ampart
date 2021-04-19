from django.urls import path
from . import views

app_name='art'

urlpatterns=[
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth')
]
