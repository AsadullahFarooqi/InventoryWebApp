import datetime

from django import forms

from .models import (
					StoreEmployers,
					Customer,
					Supplier,
					Products,
					# ContainersTypes,
					Imported,
					Exported,
					PaymentsOfCustomers,
					PaymentsToSuppliers,
					EmployersLedger,
						)


this_year = datetime.date.today().year + 1

class EmployerForm(forms.ModelForm):

	class Meta:
		model = StoreEmployers
		exclude = ["store", "timestamp", "slug", "active"]

class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		exclude = ["store", "timestamp", "slug", "active"]


class SupplierForm(forms.ModelForm):

	class Meta:
		model = Supplier
		exclude = ["store",  "timestamp", "slug", "active"]


class ProductsForm(forms.ModelForm):

	class Meta:
		model = Products
		exclude = ["store",  "timestamp", "slug", "active"]

# class ContainersTypesForm(forms.ModelForm):

# 	class Meta:
# 		model = ContainersTypes
# 		exclude = ["store",  "timestamp", "slug"]

class ImportedForm(forms.ModelForm):

	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = Imported
		exclude = ["store",  "supplier", "product_name", "timestamp", "slug", "active"]

class ExportedForm(forms.ModelForm):

	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = Exported
		exclude = ["store", "customer", "product_name", "timestamp", "slug", "active"]


class CustomerPaymentForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta(object):
		model = PaymentsOfCustomers
		exclude = ["store",  "customer", "timestamp", "slug", "active"]


class SupplierPaymentForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta(object):
		model = PaymentsToSuppliers
		exclude = ["store",  "supplier", "timestamp", "slug", "active"]

class EmployersLedgerForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = EmployersLedger
		exclude = ["store", "employer", "timestamp", "slug", "active"]