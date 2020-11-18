from django.contrib import admin
from home.models import customer, transaction_details

# Register your models here.
admin.site.register(customer)
admin.site.register(transaction_details)