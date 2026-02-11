from django.db import models

# Create your models here.




class DBG(models.Model):
    id_dbg = models.IntegerField(verbose_name='id_DBG', unique=True, blank=True)
    name = models.CharField(verbose_name='Наименование группы', max_length=50, blank=False)
    nameFull = models.CharField(verbose_name='Полное наименование группы', max_length=150, blank=True)
    name2 = models.CharField(verbose_name='Наименование группы вар2', max_length=50, blank=True)
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name='Родительская группа')
    is_active = models.BooleanField(default=True, blank=False)
    # класс для админки
    class Meta:
        ordering = ['-id']  # сортировка по полю "id" в обратном порядке
        verbose_name = 'Группа' # Как должна называться БД(модель) в единственном числе
        verbose_name_plural = 'Группы' # Как должна называться БД(модель) во множественном числе
    def __str__(self) -> str:
        return self.name