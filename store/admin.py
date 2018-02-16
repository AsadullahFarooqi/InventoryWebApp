from django.contrib import admin

from .models import (
					Store,
					Customer,
					Supplier,
					Products,
					ContainersTypes,
					Imported,
					Exported,
					PaymentsToSuppliers,
					PaymentsOfCustomers,
						)


# Register your models here.
admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Products)
admin.site.register(Imported)
admin.site.register(Exported)
admin.site.register(ContainersTypes)
admin.site.register(PaymentsToSuppliers)
admin.site.register(PaymentsOfCustomers)
