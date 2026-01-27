from django.db import models

# Create your models here.




class DBG(models.Model):
    # id_dbg = models.IntegerField(verbose_name='id_DBG', primary_key=True, unique=True)
    id_dbg = models.IntegerField(verbose_name='id_DBG', unique=True)
    name = models.CharField(verbose_name='Наименование группы', max_length=50)
    nameFull = models.CharField(verbose_name='Полное наименование группы', max_length=150)
    name2 = models.CharField(verbose_name='Наименование группы вар2', max_length=50)
    # id_parent = models.IntegerField(verbose_name='id_Родительская группа', null=True)# id_parent INTEGER,
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name='Родительская группа')
    is_active = models.BooleanField(default=False)
    class Meta:
        ordering = ['-id']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    def __str__(self) -> str:
        return self.name