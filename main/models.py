from django.db import models
from django.shortcuts import reverse


class AllItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.price)


# class TestBurner(models.Model):
#     item = models.ForeignKey(AllItems, on_delete=models.CASCADE, blank=True)
#     power = models.FloatField()
#
#     def __str__(self):
#         return str(self.item)


# class TestGorelka(models.Model):
#     item = models.ForeignKey(AllItems, on_delete=models.CASCADE, blank=True)
#     autoburn = models.BooleanField()
#
#     def __str__(self):
#         return str(self.item)


class Burner(models.Model):
    item = models.ForeignKey('AllItems', on_delete=models.CASCADE, verbose_name='Предмет')
    # photo_main = models.ImageField(upload_to='photos/', verbose_name='Фото 1')
    # photo_second = models.ImageField(upload_to='photos/', verbose_name='Фото 2')
    # photo_third = models.ImageField(upload_to='photos/', verbose_name='Фото 3', blank=True)
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

    # def save(self, *args, **kwargs):
    #     self.category_id = 1
    #     super(Burner, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.item)


class Heater(models.Model):
    item = models.ForeignKey('AllItems', on_delete=models.CASCADE, verbose_name='Предмет')
    upload_at = models.DateTimeField(auto_now_add=True)

    fuel = models.CharField(max_length=20, verbose_name='Тип топлива')
    fuel_consumption = models.IntegerField(verbose_name='Расход топлива')
    boiling_time = models.FloatField(verbose_name='Время закипания')
    size_x = models.IntegerField(verbose_name='Длина')
    size_y = models.IntegerField(verbose_name='Ширина')
    size_z = models.IntegerField(verbose_name='Высота')
    weight = models.FloatField(verbose_name='Вес')
    piezo_ignition = models.BooleanField(verbose_name='Пьезоподжиг')
    material = models.CharField(max_length=50, verbose_name='Материал')
    power = models.FloatField(verbose_name='Мощность')

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
    image = models.ImageField(upload_to='photos/' + str(item) + '/', verbose_name='Фото')

    def __str__(self):
        return str(self.image)

    
