from django.core.validators import MaxValueValidator
from django.db import models

from BaseData.models import Champion, Item, Augment, BasicItem


class ItemizedUnit(models.Model):
    id         = models.AutoField(primary_key=True)
    champ      = models.ForeignKey(Champion, on_delete=models.CASCADE)
    item_1     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='first_item', null=True)
    item_2     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='second_item', null=True)
    item_3     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='third_item', null=True)
    star_level = models.IntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return f"{self.star_level} start {self.champ} with items {self.item_1}, {self.item_2}, {self.item_3}"


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    first_champ           = models.ForeignKey(Champion, on_delete=models.CASCADE, limit_choices_to={'value': 1}, null=True)
    first_item            = models.ForeignKey(BasicItem, on_delete=models.CASCADE, null=True)
    augment_1             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='first_augment')
    augment_2             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='second_augment')
    augment_3             = models.ForeignKey(Augment, on_delete=models.CASCADE, related_name='third_augment', null=True)

    champ_1               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='first_champ')
    champ_2               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='second_champ', null=True)
    champ_3               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='third_champ', null=True)
    champ_4               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='fourth_champ', null=True)
    champ_5               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='fifth_champ', null=True)
    champ_6               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='sixth_champ', null=True)
    champ_7               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='seventh_champ', null=True)
    champ_8               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='eight_champ', null=True)
    champ_9               = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='ninth_carry', null=True)
    champ_10              = models.ForeignKey(ItemizedUnit, on_delete=models.CASCADE, related_name='tenth_champ', null=True)


    placement             = models.IntegerField(validators=[MaxValueValidator(8)])
    final_level           = models.IntegerField(validators=[MaxValueValidator(10)])
    patch                 = models.CharField(default="No added", max_length=255)
    tft_set_number        = models.CharField(default="7", max_length=255)





