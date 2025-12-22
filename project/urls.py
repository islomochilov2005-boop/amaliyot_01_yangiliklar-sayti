from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]