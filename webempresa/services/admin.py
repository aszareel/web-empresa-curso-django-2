from django.contrib import admin
from .models import Services

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Services, ServiceAdmin)