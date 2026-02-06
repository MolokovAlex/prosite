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
    itemGroup = None
    if request.method == 'POST': # если отправили данные с формы сюда, в backend
        # name = request.POST.get("name", "Undefined")
        if request.POST.get("radioSwitch"):
            pkGroup = request.POST.get("radioSwitch", 3)    # какой радио-переключатель был выбран ?
            itemGroup = DBG.objects.get(id=pkGroup)         # считаем этот элемент таблицы
        if request.POST.get("buttonDelete"):
            pkItem = request.POST.get("itemPk")    # какой радио-переключатель был выбран ?
            itemDelGroup = DBG.objects.get(id=pkItem)         # считаем этот элемент таблицы
            itemDelGroup.delete()
        if request.POST.get("buttonCreate"):
            itemDBG = DBG()
            # itemDBG.pk = int(request.POST.get("itemPk", 99999))  
            itemDBG.id_dbg = 99999
            itemDBG.name = request.POST.get("itemName", "_")  
            itemDBG.nameFull = request.POST.get("itemNameFull", "_")  
            itemDBG.name2 = request.POST.get("itemName2", "_") 
            # itemDBG.is_active = request.POST.get("itemIsActive", True)
            itemDBG.save() 
            itemDBG.id_dbg = itemDBG.pk
            itemDBG.save() 
    else:       #  GET получаем форму на монитор
        pass

    dbcAll = DBG.objects.all()
    data_in_template_editDBG= {
        'dbcAll': dbcAll,
        'itemGroup':itemGroup,
        # 'name': name,
        'title': 'Список групп',
    }
    return render(request, 'editDBG.html', data_in_template_editDBG)