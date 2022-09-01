from django.contrib import admin

from apps.products.models import *
# Register your models here.
admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Indicator)
admin.site.register(Country)
admin.site.register(Color)
admin.site.register(Business)
admin.site.register(Size)
admin.site.register(Reference)
admin.site.register(Product)
admin.site.register(Size_Product)
admin.site.register(Color_Product)
admin.site.register(Business_Product)
admin.site.register(Sex_Business)

