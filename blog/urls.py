from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('blog/', views.ArticleListView.as_view(), name='blog'),
]
