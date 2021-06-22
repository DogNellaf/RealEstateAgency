from django.shortcuts import render
from django.http import HttpResponse
from .models import Estate, EstateType, Gallery, Query


# Стартовая страница
def index(request):
    if request.method == "POST":
        if request.POST.get("name") != '' and request.POST.get("mobile") != '':
            query = Query()
            print(request.POST.get("name"))
            query.name = request.POST.get("name")
            query.mobile = request.POST.get("mobile")

            if request.POST.get("sell") == "on":
                query.sell = True
            else:
                query.sell = False

            if request.POST.get("legalization") == "on":
                query.legalization = True
            else:
                query.legalization = False

            if request.POST.get("buy") == "on":
                query.buy = True
            else:
                query.buy = False

            if request.POST.get("cadastre") == "on":
                query.cadastre = True
            else:
                query.cadastre = False

            if request.POST.get("rent") == "on":
                query.rent = True
            else:
                query.rent = False

            if request.POST.get("juridical") == "on":
                query.juridical = True
            else:
                query.juridical = False

            query.other = request.POST.get("other")
            query.save()
    return render(request, "index.html")


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