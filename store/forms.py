import datetime

from django import forms

from .models import (
					Customer,
					Supplier,
					Store,
					Products,
					ContainersTypes,
					Imported,
					Exported,
					PaymentsOfCustomers,
					PaymentsToSuppliers,
						)


this_year = datetime.date.today().year


class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		exclude = ["store", "timestamp", "slug"]


class SupplierForm(forms.ModelForm):

	class Meta:
		model = Supplier
		exclude = ["store",  "timestamp", "slug"]


class ProductsForm(forms.ModelForm):

	class Meta:
		model = Products
		exclude = ["store",  "timestamp", "slug"]

class ContainersTypesForm(forms.ModelForm):

	class Meta:
		model = ContainersTypes
		exclude = ["store",  "timestamp", "slug"]

class ImportedForm(forms.ModelForm):

	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = Imported
		exclude = ["store",  "containers_still_exists", "timestamp", "slug"]

class ExportedForm(forms.ModelForm):

	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = Exported
		exclude = ["store", "timestamp", "slug"]


class ExportPaymentsForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta(object):
		model = PaymentsOfCustomers
		exclude = ["store",  "customer", "timestamp", "slug"]


class ImportPaymentsForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta(object):
		model = PaymentsToSuppliers
		exclude = ["store",  "supplier", "timestamp", "slug"]


