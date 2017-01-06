from __future__ import unicode_literals
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract=True

##### KITCHEN #####
class KType(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name='Type Name')
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_type")

    def __unicode__(self):
        return self.name

    class Meta:
            db_table = "%s_%s" % ('core', "kitchen_type")
            verbose_name = 'Kitchen Type'
            verbose_name_plural = 'Kitchen Types'
            ordering = ['name']

class Kitchen(BaseModel):
    type = models.ForeignKey(KType, on_delete=models.CASCADE, related_name='type')
    name = models.CharField(max_length=30, verbose_name='Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    l = models.IntegerField(verbose_name='length')
    b = models.IntegerField(verbose_name='breadth')
    h = models.IntegerField(verbose_name='height')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen")
        verbose_name = 'Kitchen'
        verbose_name_plural = 'Kitchens'
        ordering = ['name', 'type']

class KIncludes(BaseModel):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    items = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    size = models.CharField(max_length=20)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', 'kitchen_include')
        verbose_name = 'Kitchen Include'
        verbose_name_plural = 'Kitchen Includes'
        ordering = ['kitchen', 'name', 'brand']

class KAppliance(BaseModel):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    image = models.ImageField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_appliance")
        verbose_name = 'Kitchen Apliance'
        verbose_name_plural = 'Kitchen Appliances'
        ordering = ['name', 'kitchen']

class KMaterial(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_material")
        verbose_name = 'Kitchen material'
        verbose_name_plural = 'Kitchen Materials'
        ordering = ['name', 'price']

class KFinishing(BaseModel):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_finishing")
        verbose_name = 'Kitchen Finishing'
        verbose_name_plural = 'Kitchen Finishings'
        ordering = ['name']

class KColor(BaseModel):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_color")
        verbose_name = 'Kitchen Color'
        verbose_name_plural = 'Kitchen Colors'
        ordering = ['name']

class KImage(BaseModel):
    # k_option = models.ForeignKey(KOption, on_delete=models.CASCADE)
    kitchen = models.ForeignKey(Kitchen, related_name='kitchen', on_delete=models.CASCADE)
    k_color = models.ForeignKey(KColor, related_name='kithen_image', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='kitchen_images/')

    def __unicode__(self):
        return str(str(self.kitchen.name) + '_' + str(self.k_color.name) + '_' + str(self.id))

        # return str(self.kitchen.name + '_' + self.id)
        # db_table = "%s_%s" %  ('core', 'kitchen_image')

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_image")
        verbose_name = 'Kitchen Image'
        verbose_name_plural = 'Kitchen Images'
        ordering = ['kitchen', 'k_color']

##### KITCHEN END #####



# ##### WARDROBE #####
class WType(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name='Type Name')
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_type")

    def __unicode__(self):
        return self.name

    class Meta:
            db_table = "%s_%s" % ('core', "wardrobe_type")
            verbose_name = 'wardrobe Type'
            verbose_name_plural = 'Wardrobe Types'
            ordering = ['name']

class Wardrobe(BaseModel):
    type = models.ForeignKey(WType, on_delete=models.CASCADE, related_name='type')
    name = models.CharField(max_length=30, verbose_name='Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    # size = models.ForeignKey(KSize, verbose_name='Size')
    l = models.IntegerField(verbose_name='length')
    b = models.IntegerField(verbose_name='breadth')
    h = models.IntegerField(verbose_name='height')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe")
        verbose_name = 'Wardrobe'
        verbose_name_plural = 'Wardrobe'
        ordering = ['name', 'type']

class WIncludes(BaseModel):
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    items = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    size = models.CharField(max_length=20)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', 'wardrobe_include')
        verbose_name = 'Wardrobe Include'
        verbose_name_plural = 'Wardrobe Includes'
        ordering = ['wardrobe', 'name', 'brand']

class WAppliance(BaseModel):
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    image = models.ImageField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_appliance")
        verbose_name = 'Wardrobe Apliance'
        verbose_name_plural = 'Wardrobe Appliances'
        ordering = ['name', 'wardrobe']

class WMaterial(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_material")
        verbose_name = 'Wardrobe material'
        verbose_name_plural = 'Wardrobe Materials'
        ordering = ['name', 'price']

class WFinishing(BaseModel):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_finishing")
        verbose_name = 'Wardrobe Finishing'
        verbose_name_plural = 'Wardrobe Finishings'
        ordering = ['name']

class WColor(BaseModel):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_color")
        verbose_name = 'Wardrobe Color'
        verbose_name_plural = 'Wardrobe Colors'
        ordering = ['name']

class WImage(BaseModel):
    wardrobe = models.ForeignKey(Wardrobe, related_name='wardrobe', on_delete=models.CASCADE)
    w_color = models.ForeignKey(WColor, related_name='wardrobe_image', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='wardrobe_images/')

    def __unicode__(self):
        return str(str(self.wardrobe.name) + '_' + str(self.w_color.name) + '_' + str(self.id))

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_image")
        verbose_name = 'Wardrobe Image'
        verbose_name_plural = 'Wardrobe Images'
        ordering = ['wardrobe', 'w_color']

# ##### WARDROBE END #####
