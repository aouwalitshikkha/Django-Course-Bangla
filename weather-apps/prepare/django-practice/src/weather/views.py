from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    # return HttpResponse('<h1>First Django Project</h1>')
    return render(request, 'home.html')