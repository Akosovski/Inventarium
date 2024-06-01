from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'inventory/home.html')