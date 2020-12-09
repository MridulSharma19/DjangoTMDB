from django.shortcuts import render
import requests

# Create your views here.

def top(request):
    response=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'toprated.html',{"data":data})

def popular(request):
    response=requests.get('https://api.themoviedb.org/3/movie/popular?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'popular.html',{"data":data})    

def now(request):
    response=requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'nowplaying.html',{"data":data})

def upcoming(request):
    response=requests.get('https://api.themoviedb.org/3/movie/upcoming?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'upcoming.html',{"data":data})    
def details(request,id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=API_KEY&language=en-US')
    data=response.json()    
    return render(request,'detail.html',{"data":data})