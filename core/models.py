from __future__ import unicode_literals
from django.db import models
# from colorfield.fields import ColorField
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

class BaseModel(models.Model):
    """ Base Class """
    class Meta:
        abstract=True

##### KITCHEN #####

class KType(BaseModel):
    """ Model to save Kitchen Types """
    name = models.CharField(max_length=30, unique=True, verbose_name='Type Name')
    image = models.ImageField(upload_to='kitchen/images/kitchen_types/')
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KType, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
            db_table = "%s_%s" % ('core', "kitchen_type")
            verbose_name = 'Kitchen Type'
            verbose_name_plural = 'Kitchen Types'
            ordering = ['name']

class KTheme(BaseModel):
    """ Model to save sub-category of Kitchen Types """
    k_type = models.ForeignKey(KType, on_delete=models.CASCADE, related_name='k_type')
    name = models.CharField(max_length=30, verbose_name='Theme Name')
    desc = models.CharField(max_length=100, verbose_name='Description')
    image = models.ImageField(upload_to='kitchen/images/kitchen_themes/')
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return (self.k_type.name + ' - ' + self.name)

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KTheme, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
            db_table = "%s_%s" % ('core', "kitchen_theme")
            verbose_name = 'Kitchen Theme'
            verbose_name_plural = 'Kitchen Themes'
            ordering = ['name']
            unique_together = ('k_type', 'slug')


class Kitchen(BaseModel):
    """ Model to save kitchen detail """
    theme = models.ForeignKey(KTheme, on_delete=models.CASCADE, related_name='Theme')
    name = models.CharField(max_length=30, verbose_name='Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    l = models.IntegerField(verbose_name='Length')
    b = models.IntegerField(verbose_name='Breadth')
    h = models.IntegerField(verbose_name='Height')
    base_price = models.IntegerField(verbose_name='Base Price')
    min_change = models.IntegerField(default=20, verbose_name='Miniumum Change')
    max_change = models.IntegerField(default=40, verbose_name='Maximum Change')
    slug = models.SlugField(max_length=200, null=True, editable=False)

    def __unicode__(self):
        return (self.theme.name + '_' + self.name + '_' + str(self.l) + 'x' + str(self.b) + 'x' + str(self.h))

    def save(self, *args, **kwargs):
        self.slug = slugify('-'.join((self.name, 'x'.join((str(self.l), str(self.b), str(self.h))))))
        super(Kitchen, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file after the model
        storage, path = self.image.storage, self.image.path
        super(Kitchen, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen")
        verbose_name = 'Kitchen'
        verbose_name_plural = 'Kitchens'
        ordering = ['name', 'theme']
        unique_together = ('theme', 'slug', 'l', 'b', 'h')

class KIncludes(BaseModel):
    """ Model to save what kitchen includes """
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    # items = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    # size = models.CharField(max_length=20, default='1*2*3')
    image = models.ImageField(upload_to='kitchen/images/kitchen_appliances/')

    def __unicode__(self):
        return self.category

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KIncludes, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', 'kitchen_include')
        verbose_name = 'Kitchen Include'
        verbose_name_plural = 'Kitchen Includes'
        ordering = ['kitchen', 'category', 'brand']

class KISub(BaseModel):
    k_includes = models.ForeignKey(KIncludes, on_delete = models.CASCADE)
    sub_category = models.CharField(max_length=30)
    is_included = models.BooleanField(default=True)

    def __unicode__(self):
        return  (self.k_includes.category + self.sub_category)

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_includes_sub_category")
        verbose_name = 'Kitchen Includes Sub-Category'
        verbose_name_plural = 'Kitchen Includes Sub-Categories'
        ordering = ('k_includes', 'sub_category')
        unique_together = ('k_includes', 'sub_category')

class KAppliance(BaseModel):
    """ Model to save what kitchen appliances """
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kitchen/images/kitchen_appliances/')

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KAppliance, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_appliance")
        verbose_name = 'Kitchen Appliance'
        verbose_name_plural = 'Kitchen Appliances'
        ordering = ('name', 'kitchen')
        unique_together = ('kitchen', 'name')

class KMaterial(BaseModel):
    """ Model to save kitchen material """
    name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_material")
        verbose_name = 'Kitchen Material'
        verbose_name_plural = 'Kitchen Materials'
        ordering = ('name', 'price')

class KFinishing(BaseModel):
    """ Model to save finishing available for kitchen """
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_finishing")
        verbose_name = 'Kitchen Finishing'
        verbose_name_plural = 'Kitchen Finishings'
        ordering = ['name']

class KColor(BaseModel):
    """Model to save colors for kitchen """
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='kitchen/images/kitchen_color/')
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KColor, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_color")
        verbose_name = 'Kitchen Color'
        verbose_name_plural = 'Kitchen Colors'
        ordering = ['name']

class KImage(BaseModel):
    """ Model to save kitchen images based on color """
    # k_option = models.ForeignKey(KOption, on_delete=models.CASCADE)
    kitchen = models.ForeignKey(Kitchen, related_name='kitchen', on_delete=models.CASCADE)
    k_color = models.ForeignKey(KColor, related_name='kithen_image', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='kitchen/images/kitchen_images/')

    def __unicode__(self):
        return str(str(self.kitchen.name) + '_' + str(self.k_color.name) + '_' + str(self.id))

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KImage, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "kitchen_image")
        verbose_name = 'Kitchen Image'
        verbose_name_plural = 'Kitchen Images'
        ordering = ['kitchen', 'k_color']

##### KITCHEN END #####

##### WARDROBE #####

class WType(BaseModel):
    """ Model to save Wardrobe Types """
    name = models.CharField(max_length=30, unique=True, verbose_name='Type Name')
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_types/')
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(WType, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
            db_table = "%s_%s" % ('core', "wardrobe_type")
            verbose_name = 'Wardrobe Type'
            verbose_name_plural = 'Wardrobe Types'
            ordering = ['name']

class WTheme(BaseModel):
    """ Model to save sub-category of Wardrobe Types """
    w_type = models.ForeignKey(WType, on_delete=models.CASCADE, related_name='w_type')
    name = models.CharField(max_length=30, verbose_name='Theme Name')
    desc = models.CharField(max_length=100, verbose_name='Description')
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_themes/')
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return (self.w_type.name + ' - ' + self.name)

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(WTheme, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
            db_table = "%s_%s" % ('core', "wardrobe_theme")
            verbose_name = 'Wardrobe Theme'
            verbose_name_plural = 'Wardrobe Themes'
            ordering = ['name']
            unique_together = ('w_type', 'slug')

class Wardrobe(BaseModel):
    """ Model to save wardrobe detail """
    theme = models.ForeignKey(WTheme, on_delete=models.CASCADE, related_name='theme')
    name = models.CharField(max_length=30, verbose_name='Name')
    desc = models.CharField(max_length=100, verbose_name="Description")
    l = models.IntegerField(verbose_name='length')
    b = models.IntegerField(verbose_name='breadth')
    h = models.IntegerField(verbose_name='height')
    base_price = models.IntegerField(verbose_name='Base Price')
    min_change = models.IntegerField(default=20, verbose_name='Miniumum Change')
    max_change = models.IntegerField(default=40, verbose_name='Maximum Change')
    slug = models.SlugField(max_length=200, null=True, editable=False)

    def __unicode__(self):
        return (self.theme.name + '_' + self.name + '_' + str(self.l) + 'x' + str(self.b) + 'x' + str(self.h))

    def save(self, *args, **kwargs):
        self.slug = slugify('-'.join((self.name, 'x'.join((str(self.l), str(self.b), str(self.h))))))
        super(Wardrobe, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file after the model
        storage, path = self.image.storage, self.image.path
        super(Wardrobe, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe")
        verbose_name = 'Wardrobe'
        verbose_name_plural = 'Wardrobes'
        ordering = ['name', 'theme']
        unique_together = ('theme', 'slug', 'l', 'b', 'h')


class WIncludes(BaseModel):
    """ Model to save what wardrobe includes """
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    # items = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    # size = models.CharField(max_length=20)
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_appliances/')

    def __unicode__(self):
        return self.category

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(WIncludes, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', 'wardrobe_include')
        verbose_name = 'Wardrobe Include'
        verbose_name_plural = 'Wardrobe Includes'
        ordering = ['wardrobe', 'category', 'brand']

class WISub(BaseModel):
    w_includes = models.ForeignKey(WIncludes, on_delete = models.CASCADE)
    sub_category = models.CharField(max_length=30)
    is_included = models.BooleanField(default=True)

    def __unicode__(self):
        return  (self.w_includes.category + self.sub_category)

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_includes_sub_category")
        verbose_name = 'Wardrobe Includes Sub-Category'
        verbose_name_plural = 'Wardrobe Includes Sub-Categories'
        ordering = ('w_includes', 'sub_category')
        unique_together = ('w_includes', 'sub_category')

class WAppliance(BaseModel):
    """ Model to save what wardrobe appliances """
    wardrobe = models.ForeignKey(Wardrobe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_appliances/')

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(WAppliance, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_appliance")
        verbose_name = 'Wardrobe Appliance'
        verbose_name_plural = 'Wardrobe Appliances'
        ordering = ('name', 'wardrobe')
        unique_together = ('wardrobe', 'name')

class WMaterial(BaseModel):
    """ Model to save wardrobe material """
    name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_material")
        verbose_name = 'Wardrobe material'
        verbose_name_plural = 'Wardrobe Materials'
        ordering = ('name', 'price')

class WFinishing(BaseModel):
    """ Model to save finishing available for wardrobe """
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_finishing")
        verbose_name = 'Wardrobe Finishing'
        verbose_name_plural = 'Wardrobe Finishings'
        ordering = ['name']

class WColor(BaseModel):
    """Model to save colors for wardrobe """
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_color/')
    price = models.IntegerField()

    def __unicode__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(KColor, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_color")
        verbose_name = 'Wardrobe Color'
        verbose_name_plural = 'Wardrobe Colors'
        ordering = ['name']

class WImage(BaseModel):
    """ Model to save wardrobe images based on color """
    wardrobe = models.ForeignKey(Wardrobe, related_name='wardrobe', on_delete=models.CASCADE)
    w_color = models.ForeignKey(WColor, related_name='wardrobe_image', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='wardrobe/images/wardrobe_images/')

    def __unicode__(self):
        return str(str(self.wardrobe.name) + '_' + str(self.w_color.name) + '_' + str(self.id))

    def delete(self, *args, **kwargs):
        # onveriding delete method to ensure that file is deleted along with database entry
        storage, path = self.image.storage, self.image.path
        super(WImage, self).delete(*args, **kwargs)
        storage.delete(path)

    class Meta:
        db_table = "%s_%s" % ('core', "wardrobe_image")
        verbose_name = 'Kitchen Image'
        verbose_name_plural = 'Wardrobe Images'
        ordering = ['wardrobe', 'w_color']

##### WARDROBE END #####


##### FROMS #####
class KitchenResponse(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    kitchen = models.ForeignKey(Kitchen)
    material = models.ForeignKey(KMaterial)
    finishing = models.ForeignKey(KFinishing)
    color = models.ForeignKey(KColor)

class WardrobeReponse(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    wardrobe = models.ForeignKey(Wardrobe)
    material = models.ForeignKey(WMaterial)
    finishing = models.ForeignKey(WFinishing)
    color = models.ForeignKey(WColor)
##### END FORMS #####
