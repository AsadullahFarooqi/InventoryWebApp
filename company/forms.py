import datetime
from django import forms

from store.models import Store
from .models import Company


this_year = datetime.date.today().year

class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		exclude = ["owner", "timestamp", "slug"]

class StoreForm(forms.ModelForm):

	store_is_active_from = forms.DateField(widget=forms.SelectDateWidget(years = tuple(range(this_year - 40, this_year))))
	class Meta:
		model = Store
		exclude = ["company" ,"store_active", "timestamp", "slug"]
