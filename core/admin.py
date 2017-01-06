from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from core.models import *

##### KITCHEN #####

class KImageInline(NestedStackedInline):
    model=KImage
    extra=0
    fk_name='kitchen'

class KitchenAdmin(NestedModelAdmin):
    """Kitchen Admin class"""
    inlines=[
        KImageInline,
    ]

##### KITCHEN END #####

##### KITCHEN #####

class WImageInline(NestedStackedInline):
    model=WImage
    extra=0
    fk_name='wardrobe'

class WardrobeAdmin(NestedModelAdmin):
    """Wardrobe Admin class"""
    inlines=[
        WImageInline,
    ]

##### END KITCHEN #####




# class TeamInline(NestedStackedInline):
#     """Class for the team inline"""
#     model=Team
#     extra=0
#
#
# class UpdatePhotosInline(NestedStackedInline):
#     model=UpdatePhotos
#     extra=1
#     fk_name='update'
#
#
# class UpdateInline(NestedStackedInline):
#     """Class for the inline of project Updates """
#     model=Update
#     extra=0
#     inlines = [UpdatePhotosInline]
#     fk_name='project'
#
# class ProjectAdmin(NestedModelAdmin):
#     """Project Admin class"""
#     inlines=[
#         TeamInline,
#         UpdateInline,
#     ]
admin.site.register(KType)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(KIncludes)
admin.site.register(KAppliance)
admin.site.register(KMaterial)
admin.site.register(KFinishing)
admin.site.register(KColor)
admin.site.register(KImage)


admin.site.register(WType)
admin.site.register(Wardrobe, WardrobeAdmin)
admin.site.register(WIncludes)
admin.site.register(WAppliance)
admin.site.register(WMaterial)
admin.site.register(WFinishing)
admin.site.register(WColor)
admin.site.register(WImage)
