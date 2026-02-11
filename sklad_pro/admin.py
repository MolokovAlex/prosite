from django.contrib import admin

# Register your models here.

# импортирование из моделей БД DBG
from .models import DBG


class DBGAdmin (admin.ModelAdmin):
    # какие поля нужны для отображения в админке
    list_display = ('id_dbg', 'name', 'nameFull', 'name2', 'id_parent', 'is_active')
    # какие поля нужны как ссылки
    list_display_links = ('id_dbg', 'name')
    # по каким полям можно сортировать (и появиться поле для поиска)
    search_fields = ('id_dbg', 'name', 'id_parent', 'is_active')

# регистрация в админке БД DBG и полей модели
admin.site.register(DBG, DBGAdmin)