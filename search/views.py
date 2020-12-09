from django.shortcuts import render
import requests

# Create your views here.
def search(request,query):
    response= requests.get(f"https://api.themoviedb.org/3/search/multi?api_key=API_KEY&language=en-US&query={query}&page=1&include_adult=false")
    data=response.json()
    return render(request, 'searchresult.html',{"data":data})

   