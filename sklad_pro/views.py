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
    if request.method == 'POST': # если отправили данные с формы сюда, в backend
        # name = request.POST.get("name", "Undefined")
        idGroup = request.POST.get("table_dbg", 3)
        itemGroup = DBG.objects.get(id=idGroup)
    else:       #  GET получаем форму на монитор
        itemGroup = None

    dbcAll = DBG.objects.all()
    data_in_template_editDBG= {
        'dbcAll': dbcAll,
        'itemGroup':itemGroup,
        # 'name': name,
        'title': 'Список групп',
    }
    return render(request, 'editDBG.html', data_in_template_editDBG)