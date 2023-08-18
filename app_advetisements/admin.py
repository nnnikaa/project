from django.contrib import admin
from .models import Advertisement




class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'auction', 'updated_date', 'img_image']
    list_filter = ['created_at', 'auction']


admin.site.register(Advertisement, AdvertisementAdmin)




# Register your models here.
