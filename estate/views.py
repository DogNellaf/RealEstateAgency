from django.shortcuts import render

# Стартовая страница
def index(request):
    return render(request, 'index.html')