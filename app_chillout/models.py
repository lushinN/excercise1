from django.db import models
from django.contrib import admin
from  django.utils import timezone

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    descrtiption = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    acution = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return 'Сегодня в ' + str(created_time)
        else:
            return self.created_at.strftime('%d.%m.%y' ' в %H:%M:%S')



class Meta:
    db_table = "advertisements"

