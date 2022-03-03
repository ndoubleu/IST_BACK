from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
class CompanyModel(models.Model):
    name = models.CharField(verbose_name='Имя фирма', max_length=255, unique=True)
    ceo = models.CharField(verbose_name='Директор',max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    email = models.EmailField(verbose_name='Почта', max_length=255)
    website = models.URLField(verbose_name='Веб сайт')
    phone_number = models.IntegerField(verbose_name='Номер телефона', validators=[RegexValidator(regex='^998\d{9}$', message='Неверный формат номера телефона')])
    author = models.ForeignKey(get_user_model(), verbose_name="Пользователь",on_delete=models.PROTECT, null=True, editable=False)
    def __str__(self):
       return str(self.name)
       
class UsersModel(models.Model):
    passport = models.CharField(verbose_name='Серия и номер пасспорта', max_length=9, validators=[RegexValidator(regex='[A-Z]{2}[0-9]{7}', message='Неверный формат Серия пасспорта')], unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)
    job = models.CharField(verbose_name='Позиция', max_length=255)
    phone_number = models.IntegerField(verbose_name='Номер телефона', validators=[RegexValidator(regex='^998\d{9}$', message='Неверный формат номера телефона')], unique=True)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), verbose_name="Пользователь",on_delete=models.PROTECT, null=True, editable=False)
    def __str__(self):
       return str(f'{self.first_name} {self.last_name} {self.middle_name}')