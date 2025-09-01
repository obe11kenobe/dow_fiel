from django.db import models

class Data(models.Model):
    nomenclature = models.CharField(max_length=100, verbose_name='Номенклатура', db_index=True)
    document_number = models.CharField(max_length=50, verbose_name='Номер документа', db_index=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    old_order = models.CharField(max_length=50, verbose_name='Старый заказ', blank=False, null=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    resource = models.CharField(max_length=50, verbose_name='Ресурс',  blank=False, null=False)
    new_order = models.CharField(max_length=50, verbose_name='Новый заказ',  blank=False, null=False)

    class Meta:
        ordering = ['-date', 'document_number', ]
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.document_number} - {self.nomenclature}'