from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


from store.models import Store

from .models import Company
from .forms import CompanyForm, StoreForm
# Create your views here.

######################################################################################################################
##########################################   Create Views   ##########################################################
######################################################################################################################

class CompanyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = CompanyForm
	success_message = "Company is successfully added"

	def get_context_data(self, *args, **kwargs):
		context = super(CompanyCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Company"

		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		if not self.request.user.is_authenticated:
			return Http404

		obj.owner = self.request.user.profile

		return super(CompanyCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("company:add_store" , kwargs={"company_slug": self.object.slug})


class StoreCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = StoreForm
	success_message = "Store is successfully added"

	def get_context_data(self, *args, **kwargs):
		context = super(StoreCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Store"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.company = Company.objects.get(slug=self.kwargs["company_slug"])

		return super(StoreCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("store:dashboard", kwargs={"store_slug": self.object.slug })

######################################################################################################################
##########################################   Retrieve Views   ##########################################################
######################################################################################################################



class CompanyDetailView(LoginRequiredMixin, DetailView):
	template_name = "company/company_details.html"

	def get_object(self):
		self.object = get_object_or_404(Company, slug=self.kwargs["company_slug"])
		if not (self.object in self.request.user.profile.companies.all()):
			raise Http404
		return self.object

@login_required
def companies_list_view(request, owner_slug=None):
	# if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
	# 		raise Http404

	queryset_list = request.user.profile.companies.all() #.order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(email__icontains=query)|
				Q(location__icontains=query)
				).distinct()


	template_name = "company/companies_list.html"
	context = {

	"object_list": queryset_list,
	}

	return render(request, template_name, context)

# class CompaniesListView(LoginRequiredMixin, ListView):
# 	template_name = "company/companies_list.html"

# 	def get_queryset(self):

# 		profile = self.request.user.profile.companies
# 		return Company.objects.get(slug=slug).stores.all()



# class StoresListView(LoginRequiredMixin, ListView):
# 	template_name = "store/stores_list.html"

# 	def get_queryset(self):
# 		if not (Company.objects.get(slug=self.kwargs["company_slug"]) in self.request.user.companies.all()):
# 			raise Http404
# 		slug = self.kwargs["company_slug"]
# 		return Company.objects.get(slug=slug).stores.all()


@login_required
def stores_list_view(request, owner_slug=None, company_slug=None):
	if not (Company.objects.get(slug=company_slug) in request.user.profile.companies.all()):
			raise Http404

	queryset_list = Company.objects.get(slug=company_slug).stores.all() #.order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(address__icontains=query)|
				Q(location__icontains=query)
				).distinct()


	template_name = "store/stores_list.html"
	context = {
	"company_slug": company_slug,
	"object_list": queryset_list,
	}

	return render(request, template_name, context)


######################################################################################################################
##########################################   Update Views   ##########################################################
######################################################################################################################

class CompanyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	form_class = CompanyForm
	success_message = "Company is successfully updated"

	def get_object(self, **kwargs):
		if not (Company.objects.get(slug=self.kwargs["company_slug"]) in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Company.objects.get(slug= self.kwargs["company_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(CompanyUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Company"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		if not self.request.user.is_authenticated:
			return Http404

		obj.user = self.request.user
		return super(CompanyUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("company:company_details", kwargs={'company_slug': self.object.slug})



class StoreUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	form_class = StoreForm
	success_message = "Store is successfully updated"

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Store.objects.get(slug= self.kwargs["store_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(StoreUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Store"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.company = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(StoreUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:dashboard", kwargs={ "store_slug": self.object.slug, })
######################################################################################################################
##########################################   Delete Views   ##########################################################
######################################################################################################################

@login_required
def company_delete_view(request, owner_slug=None, company_slug=None):
	if not (Company.objects.get(slug=company_slug) in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Company, slug=company_slug)

	obj.active = False
	obj.stores.all().update(active=False)
	obj.save()
	messages.success(request, "Successfully Deleted")
	return HttpResponseRedirect(reverse_lazy("company:companies_list", kwargs={"owner_slug": owner_slug}))

@login_required
def store_delete_view(request, company_slug=None, store_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404

	obj = get_object_or_404(Store, slug=store_slug)
	company_slug = obj.company.slug

	obj.active = False
	obj.employers.all().update(active=False)
	obj.customers.all().update(active=False)
	obj.suppliers.all().update(active=False)
	obj.products.all().update(active=False)
	obj.store_imports.all().update(active=False)
	obj.store_exports.all().update(active=False)
	obj.store_customer_payments.all().update(active=False)
	obj.store_supplier_payments.all().update(active=False)
	obj.store_employers_ledger.all().update(active=False)
	obj.save()

	messages.success(request, "Successfully Deleted")

	return HttpResponseRedirect(reverse_lazy("company:stores_list", kwargs={"owner_slug":request.user.profile.slug, "company_slug": company_slug, }))
