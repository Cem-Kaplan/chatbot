from django.shortcuts import render

def showHomepage(request):
    return render(request, 'index.html')