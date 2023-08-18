from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length = 128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('Торг', help_text = 'Укажите уместен ли торг')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return 'Сегодня в' + str(created_time)
            #return format_html(
                #'<span style ="color:orange">Сегодня в {}</span>', created_time
            #)

        else:
            return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description ='Дата редактирования')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style ="color:orange">Сегодня в {}</span>', updated_time
            )

    @admin.display(description='Изображение')
    def img_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style = "width:100px; height:100px"/>'.format(self.image.url)
            )

class Meta:
    db_table = "advertisements"



 #adv55 = Advertisement(title = 'Баня',description = 'Баня из бруса', price = 200000, auction = False)
