from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """Квартира"""
    new_building = models.BooleanField('Новостройка', null=True)
    liked_by = models.ManyToManyField(
        User,
        related_name="liked_flats",
        verbose_name='Кто лайкнул',
        blank=True
    )
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    """Жалоба"""
    user = models.ForeignKey(
        User,
        verbose_name='Кто жаловался',
        related_name='complaints',
        on_delete=models.CASCADE
    )
    complained_flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира, на которую пожаловались',
        related_name='complaints',
        on_delete=models.CASCADE
    )
    text = models.TextField('Текст жалобы', blank=True)

    def __str__(self):
        return f'{self.user} - {self.complained_flat}'


class Owner(models.Model):
    """Собственник квартиры"""
    owner = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phonenumber = models.CharField(
        'Номер владельца',
        max_length=20,
        db_index=True
    )
    pure_phone = PhoneNumberField(
        'Нормализированный номер владельца',
        blank=True,
        db_index=True
    )
    flats = models.ManyToManyField(
        Flat,
        related_name="owners",
        verbose_name='Квартиры в собственности',
        db_index=True
    )

    def __str__(self):
        return self.owner
