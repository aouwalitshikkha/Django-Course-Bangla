from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')