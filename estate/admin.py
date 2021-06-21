from django.contrib import admin

from django.contrib import admin

from .models import Estate, EstateType, Gallery, Query

admin.site.register(EstateType)
admin.site.register(Query)

class GalleryInline(admin.TabularInline):
    fk_name = 'estate'
    model = Gallery

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]