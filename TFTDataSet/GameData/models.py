from django.core.validators import MaxValueValidator
from django.db import models

from BaseData.models import Champion, Item, Augment, BasicItem


class ItemizedUnit(models.Model):
    id = models.AutoField(primary_key=True)
    champ      = models.ForeignKey(Champion, on_delete=models.CASCADE)
    item_1     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='first_item', null=True)
    item_2     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='second_item', null=True)
    item_3     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='third_item', null=True)
    star_level = models.IntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return f"{self.star_level} start {self.champ} with items {self.item_1}, {self.item_2}, {self.item_3}"


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    first_champ           = models.ForeignKey(Champion, on_delete=models.CASCADE, limit_choices_to={'value': 1})
    first_item            = models.ForeignKey(BasicItem, on_delete=models.CASCADE)
    augment_1             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='first_augment')
    augment_2             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='second_augment')
    augment_3             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='third_augment', null=True)

    carry_unit            = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='first_carry')
    secondary_carry_unit  = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='secondary_carry', null=True)
    tank                  = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='primary_tank', null=True)

    placement             = models.IntegerField(validators=[MaxValueValidator(8)])
    final_level           = models.IntegerField(validators=[MaxValueValidator(10)])
    patch                 = models.DecimalField(max_digits=5, decimal_places=2, default=12.13)





