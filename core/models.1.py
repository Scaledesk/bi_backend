from __future__ import unicode_literals
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract=True

##### KITCHEN #####
class KitchenType(BaseModel):
    type = models.CharField(max_length=30, verbose_name='Kitchen Type')
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_type")

class Kitchen(BaseModel):
    type = models.ForeignKey(KitchenType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    size = models.CharField(max_length=30, verbose_name='Size')

class KitchenImage(BaseModel):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='kitchen_images/')

class KitchenAttr(BaseModel):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    unit = models.CharField(max_length=30)
    size = models.CharField(max_length=30, default= 'Not Available')
    image = models.ImageField(upload_to='kitchen_attr/')
    accessories = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_attribute")
        verbose_name = 'Kitchen Attribute'
        verbose_name_plural = 'Kitchen Attributes'


##### KITCHEN END #####



##### WARDROBE #####
class WardrobeType(BaseModel):
    type = models.CharField(max_length=30, verbose_name='Wardrobe Type')

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_type")

class Wardrobe(BaseModel):
    type = models.ForeignKey(WardrobeType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Wardrobe Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    size = models.CharField(max_length=30, verbose_name='Size')
class WardrobeImage(BaseModel):
    kitchen = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Wardrobe_images/')
class Meta:
    db_table = "%s_%s" % ('core', "wardrobe_images")
    verbose_name = 'Wardrobe Attribute'
    verbose_name_plural = 'Wardrobe Attributes'

class WardrobeAttr(BaseModel):
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    unit = models.CharField(max_length=30)
    size = models.CharField(max_length=30, default= 'Not Available')
    image = models.ImageField(upload_to='wardrobe_attr/')
    accessories = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_attribute")
        verbose_name = 'Wardrobe Attribute'
        verbose_name_plural = 'Wardrobe Attributes'
##### WARDROBE END #####
