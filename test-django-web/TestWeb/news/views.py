from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def news_home(request):
    news = Article.objects.order_by('-data')
    return render(request, 'news/news.html', {'news': news})



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Form is not valid'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)