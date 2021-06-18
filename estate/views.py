from django.shortcuts import render
from .models import Estate, EstateType, Gallery


# Стартовая страница
def index(request):
    return render(request, 'index.html')


# Контакты
def contacts(request):
    return render(request, 'contacts.html')


# О нас
def about(request):
    return render(request, 'about.html')


# Страница с переходом на подкаталоги
def catalog(request):
    return render(request, 'catalog.html')


# Каталог с домами
def apartments(request):
    name = "/ Квартиры"
    estate_type = EstateType.objects.filter(title='Квартира').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)

    count = elements.count()
    row_count = count // 3

    estate_list = []
    index = 1
    while index < count:
        estate = elements[index]
        temp_list = []
        if index == count - 1 and index % 3 != 0:
            temp_index = 0
            temp_list = []
            while temp_index < index % 3:
                temp_list.append(None)

        if index % 3 == 0:
            temp_list = [elements[index], elements[index + 1], elements[index + 2]]
        estate_list.append(temp_list)
        index += 3


    gallery_list = []
    for i in elements:
        gallery = Gallery.objects.filter(estate=i).first()
        gallery_list.append(gallery)

    return render(request, 'subcatalog.html', {'name': name, 'elements': elements, 'count': count, 'gallery': estate_list, 'row_count': row_count})


# Каталог с домами
def houses(request):
    name = "/ Дома и дачи"
    estate_type = EstateType.objects.filter(title='Дом').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)

    gallery_list = []
    for i in elements:
        gallery = Gallery.objects.filter(estate=i).first()
        gallery_list.append(gallery)

    count = Estate.objects.order_by('surface_area').filter(estate_type=estate_type).count
    return render(request, 'subcatalog.html', {'name': name, 'elements': elements, 'count': count, 'gallery': gallery_list})


# Каталог с домами
def rent(request):
    name = "/ Аренда"
    estate_type = EstateType.objects.filter(title='Аренда').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)
    count = elements.count
    return render(request, 'subcatalog.html', {'name': name, 'elements': elements, 'count': count})


# Каталог с домами
def land(request):
    name = "/ Участки"
    estate_type = EstateType.objects.filter(title='Участок').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)
    count = elements.count
    return render(request, 'subcatalog.html', {'name': name, 'elements': elements, 'count': count})


# Страница определенного объекта недвижимости
def estate(request):
    return render(request, 'estate.html')


# Услуги
def services(request):
    return render(request, 'services.html')


# Вакансии
def jobopenings(request):
    return render(request, 'jobopening.html')