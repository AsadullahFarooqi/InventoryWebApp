
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from company.models import Company

from .forms import (
EmployerForm,
CustomerForm,
SupplierForm,
ProductsForm,
# ContainersTypesForm,
ImportedForm,
ExportedForm,
CustomerPaymentForm,
SupplierPaymentForm,
EmployersLedgerForm

)

from .models import (
StoreEmployers,
Customer,
Supplier,
Store,
Products,
# ContainersTypes,
Imported,
Exported,
PaymentsToSuppliers,
PaymentsOfCustomers,
EmployersLedger,)

class EmployerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = EmployerForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(EmployerCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Employer"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		return super(EmployerCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:employers_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = CustomerForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(CustomerCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		return super(CustomerCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:customers_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = SupplierForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(SupplierCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(SupplierCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:suppliers_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class ProductsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ProductsForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductsCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Product"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(ProductsCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:products_list", kwargs={"store_slug": self.kwargs["store_slug"] })


# class ContainerTypesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
# 	template_name = "store/create_form.html"
# 	form_class = ContainersTypesForm
# 	success_message = "Successfully added!"
# 	success_url = reverse_lazy("store:list_stores")

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(ContainerTypesCreateView, self).get_context_data(*args, **kwargs)
# 		context["page_of"] = "Container Type"
# 		return context

# 	def form_valid(self, form):
# 		obj = form.save(commit=False)
# 		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])

# 		return super(ContainerTypesCreateView, self).form_valid(form)

# 	def get_success_url(self):
# 		return reverse("store:containers_types_list", kwargs={"store_slug": self.kwargs["store_slug"] })

class ImportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ImportedForm
	success_message = "Successfully added!"
	# success_url = reverse_lazy("store:list_stores")

	def get_context_data(self, *args, **kwargs):
		context = super(ImportCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Import"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.supplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])

		return super(ImportCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:suppliers_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class ExportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ExportedForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(ExportCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Export"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])

		return super(ExportCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:customers_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class CustomerPaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = CustomerPaymentForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(CustomerPaymentCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer Payment"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])

		return super(CustomerPaymentCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:customers_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class SupplierPaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = SupplierPaymentForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(SupplierPaymentCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Payments to Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.supplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])

		return super(SupplierPaymentCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:suppliers_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class EmployersLedgerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = EmployersLedgerForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(EmployersLedgerCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Employer Payments"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(EmployersLedgerCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:employers_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})

	######################################################################################################################
	##########################################   Retrieve Views   ########################################################
	######################################################################################################################

@login_required
def dashboard(request, store_slug=None):

	store = get_object_or_404(Store, slug=store_slug)
	# store = Company.objects.get(slug=company_slug).stores.get(slug=store_slug)
	if not (store.company in request.user.profile.companies.all()):
		raise Http404
	template_name = "store/dashboard.html"
	context = {
	"store": store,
	"store_slug": store_slug,
	"total_employers": Store.objects.get(slug=store_slug).employers.all().count(),
	"total_suppliers": Store.objects.get(slug=store_slug).suppliers.all().count(),
	"total_customers": Store.objects.get(slug=store_slug).customers.all().count(),
	"total_imports": Store.objects.get(slug=store_slug).store_imports.all().count(),
	"total_exports": Store.objects.get(slug=store_slug).store_exports.all().count(),
	"total_products": Store.objects.get(slug=store_slug).products.all().count(),
	# "total_types_of_containers": Store.objects.get(slug=store_slug).types_of_containers.all().count(),
	"total_import_payments": Store.objects.get(slug=store_slug).store_supplier_payments.all().count(),
	"total_export_payments": Store.objects.get(slug=store_slug).store_customer_payments.all().count(),
	"total_employers_payments": Store.objects.get(slug=store_slug).store_employers_ledger.all().count(),
	}
	return render(request, template_name, context)

@login_required
def each_day_report(request, store_slug=None):

	template_name = "store/customer_profile.html"
	context = {
	"customer": customer,
	}
	return render(request, template_name, context)

@login_required
def employer_profile_view(request, store_slug=None, emplyer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	employer = get_object_or_404(StoreEmployers, slug=emplyer_slug)

	template_name = "store/employer_profile.html"
	context = {
	"employer": employer,
	}
	return render(request, template_name, context)


@login_required
def customer_profile_view(request, store_slug=None, customer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	customer = get_object_or_404(Customer, slug=customer_slug)

	products = {}
	for i in set(customer.customer_exports.values_list("product_name", flat=True)):
		products[i] = sum(customer.customer_exports.filter(product_name=i).values_list("number_of_containers", flat=True))

	template_name = "store/customer_profile.html"
	context = {
	"customer": customer,
	"products": products
	}
	return render(request, template_name, context)


@login_required
def supplier_profile_view(request, store_slug=None, supplier_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404

	supplier = get_object_or_404(Supplier, slug=supplier_slug)

	products = {}

	for i in set(supplier.supplier_imports.values_list("product_name", flat=True)):
		products[i] = sum(supplier.supplier_imports.filter(product_name=i).values_list("number_of_containers", flat=True))


	template_name = "store/supplier_profile.html"
	context = {
	"supplier": supplier,
	"products": products
	}
	return render(request, template_name, context)

@login_required
def customer_product_imports_list(request, store_slug=None, customer_slug=None, cus_product=None):

	customer = get_object_or_404(Customer, slug=customer_slug)

	if not (customer.store.company in request.user.profile.companies.all()):
		raise Http404

	template_name = "store/exports_list.html"
	context = {
	"customer": customer.name,
	"object_list": customer.customer_exports.filter(product_name=cus_product)
	}

	return render(request, template_name, context)


@login_required
def supplier_product_imports_list(request, supplier_slug=None, sup_product=None):

	supplier = get_object_or_404(Supplier, slug=supplier_slug)

	if not (supplier.store.company in request.user.profile.companies.all()):
		raise Http404

	template_name = "store/imports_list.html"
	context = {
	"supplier": supplier.name,
	"object_list": supplier.supplier_imports.filter(product_name=sup_product)
	}

	return render(request, template_name, context)

@login_required
def import_details_view(request, store_slug=None, import_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	importt = get_object_or_404(Imported, slug=import_slug)
	template_name = "store/import_details.html"
	context = {
	"import": importt,
	}
	return render(request, template_name, context)

@login_required
def export_details_view(request, store_slug=None, export_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	export = get_object_or_404(Exported, slug=export_slug)
	template_name = "store/export_details.html"
	context = {
	"export": export,
	}
	return render(request, template_name, context)


######################### LIST VIEWS *********************************

@login_required
def employers_list_view(request, store_slug = None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
			raise Http404

	queryset_list = Store.objects.get(slug=store_slug).employers.all() #.order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(last_name__icontains=query)|
				Q(address__icontains=query)|
				Q(email__icontains=query)
				).distinct()


	template_name = "store/employers_list.html"
	context = {
	"object_list": queryset_list,
	"store_slug": store_slug,
	}

	return render(request, template_name, context)


@login_required
def customer_list_view(request, store_slug = None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
			raise Http404

	queryset_list = Store.objects.get(slug=store_slug).customers.all() #.order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(last_name__icontains=query)|
				Q(address__icontains=query)
				).distinct()


	template_name = "store/customers_list.html"
	context = {
	"object_list": queryset_list,
	"store_slug": store_slug,
	}

	return render(request, template_name, context)

@login_required
def supplier_list_view(request, store_slug = None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
			raise Http404

	queryset_list = Store.objects.get(slug=store_slug).suppliers.all() #.order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(last_name__icontains=query)|
				Q(address__icontains=query)
				).distinct()


	template_name = "store/suppliers_list.html"
	context = {
	"object_list": queryset_list,
	"store_slug": store_slug,
	}

	return render(request, template_name, context)

# class CustomerListView(LoginRequiredMixin, ListView):
# 	template_name = "store/customers_list.html"

# 	def get_queryset(self):
# 		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
# 			raise Http404

# 		slug = self.kwargs["store_slug"]
# 		return Store.objects.get(slug=slug).customers.all()

# 		# store = Store.objects.get(slug=self.kwargs["store_slug"])
# 		# return Customer.objects.all().filter(store=store)


# class SupplierListView(LoginRequiredMixin, ListView):
# 	model = Supplier
# 	template_name = "store/suppliers_list.html"

# 	def get_queryset(self):
# 		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
# 			raise Http404

# 		slug = self.kwargs["store_slug"]
# 		return Store.objects.get(slug=slug).suppliers.all()

# 		# store = Store.objects.get(slug=self.kwargs["store_slug"])
# 		# return Supplier.objects.all().filter(store=store)

class ProductsListView(LoginRequiredMixin, ListView):
	template_name = "store/products_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).products.all()

# class ContainerTypesListView(LoginRequiredMixin, ListView):
# 	template_name = "store/containers_types_list.html"

# 	def get_queryset(self):
# 		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
# 			raise Http404
# 		slug = self.kwargs["store_slug"]
# 		return Store.objects.get(slug=slug).types_of_containers.all()

class ImportedListView(LoginRequiredMixin, ListView):
	template_name = "store/imports_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_imports.all()

class ExportedListView(LoginRequiredMixin, ListView):
	template_name = "store/exports_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_exports.all()

class CustomerPaymentsListView(LoginRequiredMixin, ListView):
	template_name = "store/export_payments_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404

		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_customer_payments.all()


class SupplierPaymentsListView(LoginRequiredMixin, ListView):
	template_name = "store/import_payments_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_supplier_payments.all()


class EmployerPaymentsListView(LoginRequiredMixin, ListView):
	template_name = "store/employer_payments_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_employers_ledger.all()


######################################################################################################################
##########################################   Update Views   ##########################################################
######################################################################################################################

class EmployerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	form_class = EmployerForm
	success_message = "Update is Successfully done!."

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = StoreEmployers.objects.get(slug= self.kwargs["employer_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(EmployerUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Employer"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(EmployerUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:employer_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	form_class = CustomerForm
	success_message = "Update is Successfully done!."

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Customer.objects.get(slug= self.kwargs["customer_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(CustomerUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(CustomerUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:customers_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	form_class = SupplierForm
	success_message = "Update is Successfully done!."

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Supplier.objects.get(slug= self.kwargs["supplier_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(SupplierUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(SupplierUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:suppliers_list", kwargs={"store_slug": self.kwargs["store_slug"] })


class ProductsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	form_class = ProductsForm
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Products.objects.get(slug= self.kwargs["product_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ProductsUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Product"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(ProductsUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:products_list", kwargs={"store_slug": self.kwargs["store_slug"] })


# class ContainerTypesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
# 	form_class = ContainersTypesForm
# 	template_name = "store/update_form.html"
# 	success_message = "Update is Successfully done!."

# 	def get_object(self, **kwargs):
# 		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
# 			raise Http404
# 		self.object = ContainersTypes.objects.get(slug= self.kwargs["container_type_slug"])
# 		return self.object

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(ContainerTypesUpdateView, self).get_context_data(*args, **kwargs)
# 		context["page_of"] = "Container Type"
# 		return context

# 	def form_valid(self, form):
# 		obj = form.save(commit=False)
# 		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

# 		return super(ContainerTypesUpdateView, self).form_valid(form)

# 	def get_success_url(self):
# 		return reverse("store:containers_types_list", kwargs={"store_slug": self.kwargs["store_slug"] })

class ImportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = ImportedForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Imported.objects.get(slug= self.kwargs["import_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ImportUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Import"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.supplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])

		return super(ImportUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:imports_list", kwargs={"store_slug": self.kwargs["store_slug"],})


class ExportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = ExportedForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = Exported.objects.get(slug= self.kwargs["export_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ExportUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Export"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])

		return super(ExportUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:exports_list", kwargs={"store_slug": self.kwargs["store_slug"],})


class CustomerPaymentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = CustomerPaymentForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = PaymentsOfCustomers.objects.get(slug = self.kwargs["payment_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(CustomerPaymentUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer Payment"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])

		return super(CustomerPaymentUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:export_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class SupplierPaymentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = SupplierPaymentForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = PaymentsToSuppliers.objects.get(slug= self.kwargs["payment_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(SupplierPaymentUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Payment to Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.suppplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])

		return super(SupplierPaymentUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:import_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class EmployerPaymentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = EmployersLedgerForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = EmployersLedger.objects.get(slug= self.kwargs["payment_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(EmployerPaymentUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Payment of Employer"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(EmployerPaymentUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:employers_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})

######################################################################################################################
##########################################   Delete Views   ##########################################################
######################################################################################################################

@login_required
def employer_delete_view(request, store_slug=None, employer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(StoreEmployers, slug=employer_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Employer is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:employers_list", kwargs={'store_slug': store_slug, }))

@login_required
def customer_delete_view(request, store_slug=None, customer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Customer, slug=customer_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Customer is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:customers_list", kwargs={'store_slug': store_slug, }))

@login_required
def supplier_delete_view(request, store_slug=None, supplier_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Supplier, slug=supplier_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Supplier is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:suppliers_list", kwargs={'store_slug': store_slug, }))

@login_required
def products_delete_view(request, store_slug=None, product_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Products, slug=product_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Produtct is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:products_list", kwargs={'store_slug': store_slug, }))


# @login_required
# def container_type_delete_view(request, store_slug=None, container_type_slug=None):
# 	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
# 		raise Http404
# 	obj = get_object_or_404(ContainersTypes, slug=container_type_slug)
# 	obj.active=False

# 	messages.success(request, "Container Type is Successfully deleted!")

# 	return HttpResponseRedirect(reverse("store:containers_types_list", kwargs={'store_slug': store_slug, }))

@login_required
def import_delete_view(request, store_slug=None, import_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Imported, slug=import_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Import is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:imports_list", kwargs={"store_slug": store_slug}))

@login_required
def export_delete_view(request, store_slug=None, export_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Exported, slug=export_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Export is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:exports_list", kwargs={"store_slug": store_slug}))

@login_required
def customer_payment_delete_view(request, store_slug=None, customer_slug=None, payment_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(PaymentsOfCustomers, slug=payment_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Export Payment is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:export_payments_list", kwargs={"store_slug": store_slug,}))

@login_required
def supplier_payment_delete_view(request, store_slug=None, supplier_slug=None, payment_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(PaymentsToSuppliers, slug=payment_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Import payment is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:import_payments_list", kwargs={"store_slug": store_slug,}))


@login_required
def employer_payment_delete_view(request, store_slug=None, employer_slug=None, payment_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(StoreEmployers, slug=payment_slug)
	obj.active=False
	obj.save()

	messages.success(request, "Employer payment is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:employers_payments_list", kwargs={"store_slug": store_slug,}))
