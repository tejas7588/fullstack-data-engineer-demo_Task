from django.shortcuts import render
from django.http import HttpResponse
import requests

# Home page
def home(request):
    return HttpResponse("Hello, Django is working 🚀")

# Report page
def report(request):
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = response.json()
    except:
        joke = None
    return render(request, "report.html", {"joke": joke})
