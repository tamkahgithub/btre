from django.contrib import admin

# Register your models here.
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hir-date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_pages = 25

admin.site.register(Realtor, RealtorAdmin)

