from django.contrib import admin

from .models import Wine_Detail, Flavour, Cultivar

class FlavourInline(admin.TabularInline):
	model = Flavour

class CultivarInline(admin.TabularInline):
	model = Cultivar

class WineAdmin(admin.ModelAdmin):
	inlines = [FlavourInline]

admin.site.register(Wine_Detail, WineAdmin)
admin.site.register(Flavour)
admin.site.register(Cultivar)
