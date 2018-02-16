
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

from .forms import (
CustomerForm,
SupplierForm,
ProductsForm,
ContainersTypesForm,
ImportedForm,
ExportedForm,
ExportPaymentsForm,
ImportPaymentsForm,

)

from .models import (
Customer,
Supplier,
Store,
Products,
ContainersTypes,
Imported,
Exported,
PaymentsToSuppliers,
PaymentsOfCustomers,)


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


class ContainerTypesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ContainersTypesForm
	success_message = "Successfully added!"
	success_url = reverse_lazy("store:list_stores")

	def get_context_data(self, *args, **kwargs):
		context = super(ContainerTypesCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Container Type"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(ContainerTypesCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:containers_types_list", kwargs={"store_slug": self.kwargs["store_slug"] })

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

		return super(ImportCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:add_import_payment", kwargs={"store_slug": self.kwargs["store_slug"], "supplier_slug":self.object.supplier.slug, "import_slug": self.object.slug})


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
		obj.export_from_import = Imported.objects.get(slug=self.kwargs["import_slug"])

		return super(ExportCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:add_export_payment", kwargs={"store_slug": self.kwargs["store_slug"], "customer_slug":self.object.customer.slug, "export_slug": self.object.slug})


class ExportPaymentsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ExportPaymentsForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(ExportPaymentsCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer Payment"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])
		obj.payment_of_export = Exported.objects.get(slug=self.kwargs["export_slug"])

		return super(ExportPaymentsCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:export_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class ImportPaymentsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "store/create_form.html"
	form_class = ImportPaymentsForm
	success_message = "Successfully added!"

	def get_context_data(self, *args, **kwargs):
		context = super(ImportPaymentsCreateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Payments to Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.supplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])
		obj.payment_of_import = Imported.objects.get(slug=self.kwargs["import_slug"])

		return super(ImportPaymentsCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:import_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})

	######################################################################################################################
	##########################################   Retrieve Views   ########################################################
	######################################################################################################################

@login_required
def dashboard(request, store_slug=None):

	store = get_object_or_404(Store, slug=store_slug)
	if not (store.company in request.user.profile.companies.all()):
		raise Http404
	template_name = "store/dashboard.html"
	context = {
	"store": store,
	"store_slug": store_slug,
	"total_suppliers": Store.objects.get(slug=store_slug).suppliers.all().count(),
	"total_customers": Store.objects.get(slug=store_slug).customers.all().count(),
	"total_imports": Store.objects.get(slug=store_slug).store_imports.all().count(),
	"total_exports": Store.objects.get(slug=store_slug).store_exports.all().count(),
	"total_products": Store.objects.get(slug=store_slug).products.all().count(),
	"total_types_of_containers": Store.objects.get(slug=store_slug).types_of_containers.all().count(),
	"total_import_payments": Store.objects.get(slug=store_slug).store_import_payments.all().count(),
	"total_export_payments": Store.objects.get(slug=store_slug).store_export_payments.all().count(),
	}
	return render(request, template_name, context)

@login_required
def customer_profile_view(request, store_slug=None, customer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	customer = get_object_or_404(Customer, slug=customer_slug)
	template_name = "store/customer_profile.html"
	context = {
	"customer": customer,
	}
	return render(request, template_name, context)

@login_required
def supplier_profile_view(request, store_slug=None, supplier_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	supplier = get_object_or_404(Supplier, slug=supplier_slug)
	template_name = "store/supplier_profile.html"
	context = {
	"supplier": supplier,
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


class CustomerListView(LoginRequiredMixin, ListView):
	template_name = "store/customers_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404

		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).customers.all()

		# store = Store.objects.get(slug=self.kwargs["store_slug"])
		# return Customer.objects.all().filter(store=store)


class SupplierListView(LoginRequiredMixin, ListView):
	model = Supplier
	template_name = "store/suppliers_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).suppliers.all()

		# store = Store.objects.get(slug=self.kwargs["store_slug"])
		# return Supplier.objects.all().filter(store=store)

class ProductsListView(LoginRequiredMixin, ListView):
	template_name = "store/products_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).products.all()

class ContainerTypesListView(LoginRequiredMixin, ListView):
	template_name = "store/containers_types_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).types_of_containers.all()

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

class ExportPaymentsListView(LoginRequiredMixin, ListView):
	template_name = "store/export_payments_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404

		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_export_payments.all()


class ImportPaymentsListView(LoginRequiredMixin, ListView):
	template_name = "store/import_payments_list.html"

	def get_queryset(self):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		slug = self.kwargs["store_slug"]
		return Store.objects.get(slug=slug).store_import_payments.all()


######################################################################################################################
##########################################   Update Views   ##########################################################
######################################################################################################################




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


class ContainerTypesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	form_class = ContainersTypesForm
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = ContainersTypes.objects.get(slug= self.kwargs["container_type_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ContainerTypesUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Container Type"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])

		return super(ContainerTypesUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:containers_types_list", kwargs={"store_slug": self.kwargs["store_slug"] })

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
		obj.export_from_import = Imported.objects.get(slug=self.kwargs["import_slug"])


		return super(ExportUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:exports_list", kwargs={"store_slug": self.kwargs["store_slug"],})


class ExportPaymentsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = ExportPaymentsForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = PaymentsOfCustomers.objects.get(slug= self.kwargs["export_payment_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ExportPaymentsUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Customer Payment"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.customer = Customer.objects.get(slug=self.kwargs["customer_slug"])
		obj.payment_of_export = Exported.objects.get(slug=self.kwargs["export_slug"])

		return super(ExportPaymentsUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:export_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})


class ImportPaymentsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "store/update_form.html"
	success_message = "Update is Successfully done!."
	form_class = ImportPaymentsForm

	def get_object(self, **kwargs):
		if not (Store.objects.get(slug=self.kwargs["store_slug"]).company in self.request.user.profile.companies.all()):
			raise Http404
		self.object = PaymentsToSuppliers.objects.get(slug= self.kwargs["import_payment_slug"])
		return self.object

	def get_context_data(self, *args, **kwargs):
		context = super(ImportPaymentsUpdateView, self).get_context_data(*args, **kwargs)
		context["page_of"] = "Payment to Supplier"
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.Store = Store.objects.get(slug=self.kwargs["store_slug"])
		obj.suppplier = Supplier.objects.get(slug=self.kwargs["supplier_slug"])
		obj.payment_of_import = Imported.objects.get(slug=self.kwargs["import_slug"])

		return super(ImportPaymentsUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("store:import_payments_list", kwargs={"store_slug": self.kwargs["store_slug"]})

######################################################################################################################
##########################################   Delete Views   ##########################################################
######################################################################################################################

@login_required
def customer_delete_view(request, store_slug=None, customer_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Customer, slug=customer_slug)
	obj.delete()

	messages.success(request, "Customer is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:customers_list", kwargs={'store_slug': store_slug, }))

@login_required
def supplier_delete_view(request, store_slug=None, supplier_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Supplier, slug=supplier_slug)
	obj.delete()

	messages.success(request, "Supplier is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:suppliers_list", kwargs={'store_slug': store_slug, }))

@login_required
def products_delete_view(request, store_slug=None, product_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Products, slug=product_slug)
	obj.delete()

	messages.success(request, "Produtct is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:products_list", kwargs={'store_slug': store_slug, }))


@login_required
def container_type_delete_view(request, store_slug=None, container_type_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(ContainersTypes, slug=container_type_slug)
	obj.delete()

	messages.success(request, "Container Type is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:containers_types_list", kwargs={'store_slug': store_slug, }))

@login_required
def import_delete_view(request, store_slug=None, import_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Imported, slug=import_slug)
	obj.delete()

	messages.success(request, "Import is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:imports_list", kwargs={"store_slug": store_slug}))

@login_required
def export_delete_view(request, store_slug=None, export_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(Exported, slug=export_slug)
	obj.delete()

	messages.success(request, "Export is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:exports_list", kwargs={"store_slug": store_slug}))

@login_required
def export_payment_delete_view(request, store_slug=None, customer_slug=None, export_slug=None, export_payment_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(PaymentsOfCustomers, slug=export_payment_slug)
	obj.delete()

	messages.success(request, "Export Payment is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:export_payments_list", kwargs={"store_slug": store_slug,}))

@login_required
def import_payment_delete_view(request, store_slug=None, supplier_slug=None, import_slug=None, import_payment_slug=None):
	if not (Store.objects.get(slug=store_slug).company in request.user.profile.companies.all()):
		raise Http404
	obj = get_object_or_404(PaymentsToSuppliers, slug=import_payment_slug)
	obj.delete()

	messages.success(request, "Import payment is Successfully deleted!")

	return HttpResponseRedirect(reverse("store:import_payments_list", kwargs={"store_slug": store_slug,}))
