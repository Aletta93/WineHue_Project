from django.contrib import admin

from .models import Wine_Detail, Flavour, Cultivar, Characteristic

class FlavourInline(admin.TabularInline):
	model = Flavour

class CultivarInline(admin.TabularInline):
	model = Cultivar

class CharacterInline(admin.TabularInline):
	model = Characteristic

class WineAdmin(admin.ModelAdmin):
	inlines = [CharacterInline, FlavourInline]

class CharAdmin(admin.ModelAdmin):
	inlines = [CharacterInline]

admin.site.register(Wine_Detail, WineAdmin)
admin.site.register(Flavour)
admin.site.register(Cultivar)
admin.site.register(Characteristic)
