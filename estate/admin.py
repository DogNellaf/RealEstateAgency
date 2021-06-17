from django.contrib import admin

from django.contrib import admin

from .models import Estate, EstateType, Gallery

admin.site.register(EstateType)

class GalleryInline(admin.TabularInline):
    fk_name = 'estate'
    model = Gallery

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]