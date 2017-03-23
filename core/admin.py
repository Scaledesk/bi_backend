from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from core.models import *


##### KITCHEN #####
class KImageInline(NestedStackedInline):
    model=KImage
    extra=1
    fk_name='kitchen'

# class KApplianceInline(NestedStackedInline):
#     model=KAppliance
#     extra=1
#     fk_name='kitchen'

class KitchenAdmin(NestedModelAdmin):
    """Kitchen Admin class"""
    inlines=[
        KImageInline,
    ]

class KISubInline(NestedStackedInline):
    model = KISub
    extra=1
    fk_name='k_includes'

class KIncludesAdmin(NestedModelAdmin):
    inlines=[
        KISubInline,
    ]
##### KITCHEN END #####


##### WARDROBE #####

class WImageInline(NestedStackedInline):
    model=WImage
    extra=1
    fk_name='wardrobe'

# class WApplianceInline(NestedStackedInline):
#     model=WAppliance
#     extra=1
#     fk_name='wardrobe'
#
class WardrobeAdmin(NestedModelAdmin):
    """Kitchen Admin class"""
    inlines=[
        WImageInline,
        # WApplianceInline,
    ]

# class WISubInline(NestedStackedInline):
#     model = WISub
#     extra=1
#     fk_name='w_includes'
#
# class WIncludesAdmin(NestedModelAdmin):
#     inlines=[
#         WISubInline,
#     ]
#
##### END WARDROBE #####

admin.site.register(KType)
admin.site.register(KTheme)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(KIncludes, KIncludesAdmin)
# admin.site.register(KISub)
admin.site.register(KAppliance)
admin.site.register(KMaterial)
admin.site.register(KFinishing)
admin.site.register(KColor)
# admin.site.register(KImage)


admin.site.register(WType)
admin.site.register(WTheme)
admin.site.register(Wardrobe, WardrobeAdmin)
# admin.site.register(WIncludes, WIncludesAdmin)
# admin.site.register(WISub)
# admin.site.register(WAppliance)
admin.site.register(WMaterial)
admin.site.register(WFinishing)
admin.site.register(WColor)
# admin.site.register(WImage)

# admin.site.register(KitchenResponse)
# admin.site.register(WardrobeReponse)
