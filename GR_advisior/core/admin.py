from django.contrib import admin
from .models import Advisor
# Register your models here.
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'phone_number', 'instagram', 'position', 'collabo_number', 'address']

admin.site.register(Advisor, AdvisorAdmin)