from django.db import models


class Burner(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', blank=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    photo_main = models.ImageField(upload_to='photos/', verbose_name='Фото 1')
    photo_second = models.ImageField(upload_to='photos/', verbose_name='Фото 2', blank=True)
    photo_third = models.ImageField(upload_to='photos/', verbose_name='Фото 3', blank=True)
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

    def save(self, *args, **kwargs):
        self.category_id = 1

        super(Burner, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return str(self.category_name)
