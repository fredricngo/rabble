from django.shortcuts import render    
from django.http import HttpResponse

def index(request):
    context = {"welcome": "Hello, world!"}
    return render(request, "rabble/index.html", context)

#when the index path is accessed, the function will render the rabble/index.html template with the context provided.

def profile(request):
    return render(request, "rabble/profile.html")

#when the profile path is accessed, this function will render the rabble/profile.html template.

