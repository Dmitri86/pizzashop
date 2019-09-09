from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False, verbose_name='Логотип:')

    def __str__(self):
        return self.name



class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pizza_imsges/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


