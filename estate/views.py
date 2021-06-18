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
    temp_estate_list = []
    index = 0
    while index < count:
        if (index % 3 == 0 and index != 0) or (index == count - 1):
            estate_list.append(temp_estate_list)
            temp_estate_list = []
        temp_estate_list.append(Gallery.objects.filter(estate=elements[index]).first())
        index += 1

    estate_list.append(temp_estate_list)
    return render(request, 'subcatalog.html', {'name': name, 'elements': estate_list, 'count': count})


# Каталог с домами
def houses(request):
    name = "/ Дома и дачи"
    estate_type = EstateType.objects.filter(title='Дом').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)

    count = elements.count()
    row_count = count // 3

    estate_list = []
    temp_estate_list = []
    index = 0
    while index < count:
        if (index % 3 == 0 and index != 0) or (index == count - 1):
            estate_list.append(temp_estate_list)
            temp_estate_list = []
        temp_estate_list.append(Gallery.objects.filter(estate=elements[index]).first())
        index += 1

    estate_list.append(temp_estate_list)
    return render(request, 'subcatalog.html', {'name': name, 'elements': estate_list, 'count': count})


# Каталог с домами
def rent(request):
    name = "/ Аренда"
    estate_type = EstateType.objects.filter(title='Аренда').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)

    count = elements.count()
    row_count = count // 3

    estate_list = []
    temp_estate_list = []
    index = 0
    while index < count:
        if (index % 3 == 0 and index != 0) or (index == count - 1):
            estate_list.append(temp_estate_list)
            temp_estate_list = []
        temp_estate_list.append(Gallery.objects.filter(estate=elements[index]).first())
        index += 1

    estate_list.append(temp_estate_list)
    return render(request, 'subcatalog.html', {'name': name, 'elements': estate_list, 'count': count})


# Каталог с домами
def land(request):
    name = "/ Участки"
    estate_type = EstateType.objects.filter(title='Участок').first()
    elements = Estate.objects.order_by('surface_area').filter(estate_type=estate_type)

    count = elements.count()
    row_count = count // 3

    estate_list = []
    temp_estate_list = []
    index = 0
    while index < count:
        if (index % 3 == 0 and index != 0) or (index == count - 1):
            estate_list.append(temp_estate_list)
            temp_estate_list = []
        temp_estate_list.append(Gallery.objects.filter(estate=elements[index]).first())
        index += 1

    estate_list.append(temp_estate_list)
    return render(request, 'subcatalog.html', {'name': name, 'elements': estate_list, 'count': count})


# Страница определенного объекта недвижимости
def estate(request, title):
    obj = Estate.objects.filter(title=title).first()
    list = Gallery.objects.filter(estate=obj)
    return render(request, 'estate.html', {'gallery': list})


# Услуги
def services(request):
    return render(request, 'services.html')


# Вакансии
def jobopenings(request):
    return render(request, 'jobopening.html')