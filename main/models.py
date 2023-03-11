from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class AllItems(models.Model):
    name = models.CharField(max_length=100)
    name_lower = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name) + " " + str(self.price)

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower() if self.name else None
        return super().save(*args, **kwargs)


class Burner(models.Model):
    item = models.OneToOneField('AllItems', on_delete=models.CASCADE, verbose_name='Предмет')
    upload_at = models.DateTimeField(auto_now_add=True)

    power = models.FloatField(verbose_name='Мощность')
    material = models.CharField(max_length=50, verbose_name='Материал')
    pressure_min = models.FloatField(verbose_name='Минимальное давление')
    pressure_max = models.FloatField(verbose_name='Максимальное давление')
    autofire = models.BooleanField(verbose_name='Автоподжиг')
    weight = models.FloatField(verbose_name='Вес')
    size_x = models.IntegerField(verbose_name='Длина')
    size_y = models.IntegerField(verbose_name='Ширина')
    size_z = models.IntegerField(verbose_name='Высота')
    flame_control = models.BooleanField(verbose_name='Регулирование пламени')
    fuel_type = models.CharField(max_length=50, verbose_name='Тип топлива')

    def __str__(self):
        return str(self.item)


class Heater(models.Model):
    item = models.OneToOneField('AllItems', on_delete=models.CASCADE, verbose_name='Предмет')
    upload_at = models.DateTimeField(auto_now_add=True)

    fuel_type = models.CharField(max_length=20, verbose_name='Тип топлива', blank=True)
    fuel_consumption = models.IntegerField(verbose_name='Расход топлива', blank=True)
    boiling_time = models.FloatField(verbose_name='Время закипания', blank=True)
    size_x = models.IntegerField(verbose_name='Длина', blank=True)
    size_y = models.IntegerField(verbose_name='Ширина', blank=True)
    size_z = models.IntegerField(verbose_name='Высота', blank=True)
    weight = models.FloatField(verbose_name='Вес', blank=True)
    piezo_ignition = models.BooleanField(verbose_name='Пьезоподжиг', blank=True)
    material = models.CharField(max_length=50, verbose_name='Материал', blank=True)
    pressure = models.FloatField(verbose_name='Давление', blank=True)
    power = models.FloatField(verbose_name='Мощность', blank=True)

    def __str__(self):
        return str(self.item)


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='URL')

    def __str__(self):
        return str(self.category_name)

    def get_absolute_url(self):
        return reverse('category/', kwargs={'category_slug_items': self.slug})


class Images(models.Model):
    item = models.ForeignKey('AllItems', on_delete=models.CASCADE, verbose_name='Предмет')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')
    main_photo = models.BooleanField(default=False, verbose_name='Главное фото')

    def __str__(self):
        return str(self.image)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(AllItems, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

