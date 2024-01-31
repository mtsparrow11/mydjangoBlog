from django.shortcuts import render
from . import models
# Create your views here.

def articels_list(request):
    articles = models.Article.objects.all().order_by('date')
    
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)
