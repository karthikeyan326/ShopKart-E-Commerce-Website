from django.contrib import admin
from .models import *


# class CatagoryAdmin(admin.ModelAdmin):
#     list_display=('name','image','decription')
#     admin.site.register(Catagory,CatagoryAdmin)

admin.site.register(Catagory)
admin.site.register(Product)

