from django.shortcuts import render

# Стартовая страница
def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')
