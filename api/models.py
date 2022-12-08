from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
STATUSES = ('отправлено', 'не отправлено', 'не доставлено')


class Mailing(models.Model):
    date_mailing = models.DateTimeField(
        verbose_name=_('Дата и время рассылки'),
        help_text='Введите дату и время рассылки'
    )
    text = models.TextField(
        verbose_name=_('Текст рассылки'),
        help_text='Введите текст письма'
    )
    client_filter = models.CharField(
        verbose_name=_('Фильтр'),
        max_length=200,
        help_text='Введите фильтр по коду оператора или тэгу'
    )
    date_stop = models.DateTimeField(
        verbose_name=_('Дата и время прекращения рассылки'),
        help_text='Введите дату и время прекращения рассылки'
    )


class Client(models.Model):
    tel = PhoneNumberField(
        verbose_name=_('Телефон'),
        max_length=15,
        unique = True,
        null = False,
        blank = False,
        help_text='Введите телефонный номер'
    )
    code = models.IntegerField(
        verbose_name=_('Телефонный код оператора'),
        unique = True,
        null = False,
        blank = False,
        help_text='Введите телефонный код оператора'
    )
    tag = models.CharField(
        verbose_name='Тег',
        help_text='Введите тег',
        max_length=200
    )
    timezone = models.CharField(max_length=32, choices=TIMEZONES, 
    default='UTC')
    
    def __str__(self): 
        return self.tel


class Message(models.Model):
    date = models.DateTimeField(
        verbose_name=_('Дата и время отправки'),
    )
    status = models.CharField(max_length=32, choices=STATUSES, 
    default='не отправлено')
    id_mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete = models.SET_NULL, null = True)
    id_client = models.ForeignKey(Client, verbose_name='Клиент', on_delete = models.SET_NULL, null = True)
