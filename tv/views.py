from django.shortcuts import render
import requests

# Create your views here.
def top(request):
    response=requests.get('https://api.themoviedb.org/3/tv/top_rated?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'topratedtv.html',{"data":data})

def popular(request):
    response=requests.get('https://api.themoviedb.org/3/tv/popular?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'populartv.html',{"data":data})    

def now(request):
    response=requests.get('https://api.themoviedb.org/3/tv/airing_today?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'nowplayingtv.html',{"data":data})

def upcoming(request):
    response=requests.get('https://api.themoviedb.org/3/tv/on_the_air?api_key=API_KEY&language=en-US&page=1')
    data=response.json()
    return render(request, 'upcomingtv.html',{"data":data})    

def details(request,id):
    response=requests.get(f'https://api.themoviedb.org/3/tv/{id}?api_key=API_KEY&language=en-US')
    data=response.json()    
    return render(request,'detailtv.html',{"data":data})    