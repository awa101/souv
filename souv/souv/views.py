from django.shortcuts import render


def index_map(request):
    
    return render(request, "index.html")