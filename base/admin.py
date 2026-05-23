from django.contrib import admin
from .models import productmodel
# Register your models here.
class productadmin(admin.ModelAdmin):
    model = productmodel
    list_display =['pname','pcategory','price','pqauntity','pimage']
admin.site.register(productmodel,productadmin)