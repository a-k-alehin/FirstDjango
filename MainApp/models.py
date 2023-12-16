from django.db import models

# Create your models here.

class Color(models.Model):
    name  = models.CharField(max_length=32)
    def __repr__(self) -> str:
        return f'Color({self.name})'

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    descr = models.CharField(max_length=500, blank=True, default="нет описания")
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        colors = [c.name for c in self.colors.all()]
        return f'{self.id} {self.name} {self.brand} {self.count} {colors}'
    
