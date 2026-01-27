from django.shortcuts import render
from django.http import HttpResponse
from .models import DBG

# Create your views here.


def index(request):
    data_in_template_Index = {
        # 'catalogObjectsAll': catalog_objects_all , 
        'title': 'Сайт Производственного отдела',
        # 'sellers': sellers,
        }
    return render(request, 'index.html', context=data_in_template_Index)

# def edit_DBG(request):
#     data_in_template_Index = {
#         # 'catalogObjectsAll': catalog_objects_all , 
#         'title': 'Создание/Редактирование группы/подгруппы',
#         # 'sellers': sellers,
#         }
#     return render(request, 'editDBG.html', context=data_in_template_Index)


def edit_DBG(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    data = {
        'name': name,
        'age': age,
        }
    return render(request, 'editDBG.html', context=data)