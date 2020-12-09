from django.shortcuts import render
import requests

# Create your views here.

def home(request):
        response=requests.get('https://api.themoviedb.org/3/movie/popular?api_key=API_KEY&language=en-US&page=1')
        data=response.json()
        tvresponse=requests.get('https://api.themoviedb.org/3/tv/popular?api_key=API_KEY&language=en-US&page=1')
        tvdata=tvresponse.json()
           
        return render(request, 'home.html',{"moviedata":data,"tvdata":tvdata})  
