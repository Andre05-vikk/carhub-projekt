from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Car(models.Model):
    state_choice = (
        ('TT', 'Tartu'),
        ('TA', 'Tallinn')
    )

    year_choice = []
    for r in range(1990, (datetime.now().year+1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruse Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags')
    )
    door_choices = (
        ('2', '2'),
        ('3', '3')
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=255)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    body_style = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.year}{self.car_title}{self.model}'

