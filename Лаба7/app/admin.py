from django.contrib import admin
from.models import *




class OrdersAdmin(admin.ModelAdmin):
    fields = ('fio_customer', 'computer_model')
    list_filter = ('fio_customer', 'computer_model')
    list_display = ('fio_customer', 'computer_model')
    search_fields = ('fio_customer', 'computer_model')
    list_per_page = 10


class SubjectsAdmin(admin.ModelAdmin):
    list_per_page = 10

admin.site.register(Order, OrdersAdmin)