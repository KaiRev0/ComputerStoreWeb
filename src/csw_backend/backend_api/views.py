from django.shortcuts import render

def index(request):
    return render(request, 'backend_api/index.html')