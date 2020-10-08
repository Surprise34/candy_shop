from django.contrib import admin
from shop.models import Sweet, Manufacturer, Country, TypeOfSweet

class SweetAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'typeOfSweet', 'price_for_one', 'price_weight')
    list_select_related = ('manufacturer', 'typeOfSweet')    
    

class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ('name' , 'country')
	list_select_related = ('country', )
	
class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
class TypeOfSweetAdmin(admin.ModelAdmin):
	list_display = ('name' ,)
	
    

admin.site.register(Sweet, SweetAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(TypeOfSweet, TypeOfSweetAdmin)


# Register your models here.
