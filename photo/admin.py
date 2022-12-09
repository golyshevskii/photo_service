from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'img', 'title', 
                    'desc', 'people', 'location', 
                    'tags', 'user', 'cr_dt']


admin.site.register(Photo, PhotoAdmin)