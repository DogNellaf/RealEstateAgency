from django.shortcuts import render

# Стартовая страница
def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def catalog(request):
    return render(request, 'catalog.html')

def services(request):
    return render(request, 'services.html')

def jobopenings(request):
    return render(request, 'jobopening.html')