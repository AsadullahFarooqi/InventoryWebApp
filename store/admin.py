from django.contrib import admin

from .models import (
					Store,
					StoreEmployers,
					Customer,
					Supplier,
					Products,
					# ContainersTypes,
					Imported,
					Exported,
					PaymentsToSuppliers,
					PaymentsOfCustomers,
					EmployersLedger,
						)


# Register your models here.
admin.site.register(Store)
admin.site.register(StoreEmployers)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Products)
admin.site.register(Imported)
admin.site.register(Exported)
admin.site.register(EmployersLedger)
# admin.site.register(ContainersTypes)
admin.site.register(PaymentsToSuppliers)
admin.site.register(PaymentsOfCustomers)
