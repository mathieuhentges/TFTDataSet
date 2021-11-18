from django.core.validators import MaxValueValidator
from django.db import models


class Traits(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField(validators=[MaxValueValidator(5)])
    name  = models.CharField(max_length=250)
    traits = models.ManyToManyField(
        'Traits'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BasicItem(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=250)
    component_1 = models.ForeignKey("BasicItem", on_delete=models.CASCADE, related_name='first_component')
    component_2 = models.ForeignKey("BasicItem", on_delete=models.CASCADE, related_name='second_component')


    def __str__(self):
        return self.name

class Augment(models.Model):
    id = models.AutoField(primary_key=True)
    name   = models.CharField(max_length=250)
    rarity =  models.IntegerField([MaxValueValidator(3)])