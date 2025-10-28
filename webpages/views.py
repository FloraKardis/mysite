from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'welcome_text': "Hello, world!"})
