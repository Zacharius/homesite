from django.shortcuts import render
from django.views import generic
from .models import Article

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article
