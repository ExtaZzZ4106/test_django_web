from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'hello', '123']
    }
    print("==========================main page==========================")
    return render(request, 'main/index.html', data)
    
def about(request):
    print("==========================about page==========================")
    return render(request, 'main/about.html')