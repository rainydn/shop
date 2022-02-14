from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


from .models import *


# class MembersInline(admin.TabularInline):
#
#     model = Company.members.through


class ImageGalleryInline(GenericTabularInline):

    model = ImageGallery
    readonly_fields = ('image_url',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    inlines = [ImageGalleryInline]



admin.site.register(Genre)
# admin.site.register(Member)
admin.site.register(MediaType)
admin.site.register(Company)
admin.site.register(ImageGallery)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
