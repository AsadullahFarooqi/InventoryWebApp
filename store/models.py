from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from company.models import Company


# class AllModels(models.Manager):
#     def active(self, *args, **kwargs):
#         # Post.objects.all() = super(PostManager, self).all()
#         return super(AllModels, self).filter(active=True)


class Store(models.Model):
	company = models.ForeignKey(Company, related_name="stores")
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=250, blank=True, null=True)
	slug = models.SlugField(unique=True, blank=True, null=True)
	capacity = models.PositiveIntegerField(blank=True, null=True, help_text="containers the store can hold")
	
	timestamp = models.DateTimeField(auto_now_add=True)
	store_is_active_from = models.DateField(auto_now=False, auto_now_add=False)

	active = models.BooleanField(default=True)

	class Meta(object):
		verbose_name_plural = "Stores"
		ordering = ["-timestamp"]

	def __str__(self):
		return self.name

	def get_absolute_url(self):
	    return reverse("store:dashboard", kwargs={"slug": self.slug})

class Customer(models.Model):
	store = models.ForeignKey(Store, related_name="customers")
	name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25, blank=True, null=True)
	id_card_number = models.BigIntegerField(blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	contact = models.BigIntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add= True)
	slug = models.SlugField(unique=True, blank=True, null=True)

	# objects = AllModels()

	class Meta(object):
		verbose_name_plural = "Customers"
		ordering = ["-name"]

	@property
	def products(self):

		prod = []

		for i in self.customer_exports.values_list("product", flat=True):
			prod.append(Products.objects.get(id = i).name)

		return set(prod)
	
	@property
	def payments_should_be_paid(self):
		payments = 0
		for export in self.customer_exports.all():
			payments += export.total_price
		return payments

	@property
	def paid_payments(self):
		return sum(self.customer_payments.values_list("amount", flat=True))
	
	@property
	def payments_done_def(self):

		if self.paid_payments >= sum(self.customer_exports.values_list("total_price", flat=True)):
			return True
		else:
			return False

	def __str__(self):
		return str(self.name) + str(self.last_name)

	

class Supplier(models.Model):
	store = models.ForeignKey(Store, related_name="suppliers")
	name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25, blank=True, null=True)
	id_card_number = models.BigIntegerField(blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	contact = models.BigIntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add= True)
	slug = models.SlugField(unique=True, blank=True, null=True)

	class Meta(object):
		verbose_name_plural = "Suppliers"
		ordering = ["-name"]

	@property
	def payments_should_be_paid(self):
		payments = 0
		for importt in self.supplier_imports.all():
			payments += importt.total_price
		return payments

	@property
	def products(self):

		prod = []

		for i in self.supplier_imports.values_list("product", flat=True):
			prod.append(Products.objects.get(id = i).name)

		return set(prod)

	@property
	def paid_payments(self):
		return sum(self.supplier_payments.values_list("amount", flat=True))
	
	@property
	def payments_done_def(self):
		
		if self.paid_payments >= sum(self.supplier_imports.values_list("total_price", flat=True)):
			return True
		else:
			return False


	def __str__(self):
		return str(self.name) + str(self.last_name)


	# class Products(models.Model):
	# 	store = models.ForeignKey(Store, related_name="products")
	# 	name n = models.CharField(max_length=30)
	# 	details = models.TextField(blank=True, null=True)
	# 	slug = models.SlugField(unique=True, blank=True, null=True)
	# 	timestamp = models.DateTimeField(auto_now_add=True)

	# 	class Meta(object):
	# 		verbose_name_plural = "Products"
	# 		ordering = ["-timestamp"]

	# 	def __str__(self):
	# 		return self.name

	# def get_absolute_url(self):
	#     return reverse("store:store_details", kwargs={"slug": self.slug})

class Products(models.Model):

	store = models.ForeignKey(Store, related_name="products")
	
	name = models.CharField(max_length=50)
	product_details = models.TextField(blank=True, null=True)

	container_type_name = models.CharField(max_length=55)
	# container_use_for = models.ForeignKey(Products, related_name="contianer_types" , blank=True, null=True,)
	approximate_weight_container_holds = models.PositiveIntegerField(blank=True, null=True, help_text="Make sure the value is in kg!")
	length 		= models.PositiveIntegerField(blank=True, null=True, help_text="Make sure the value is in inches!")
	width 		= models.PositiveIntegerField(blank=True, null=True, help_text="Make sure the value is in inches!")
	depth 		= models.PositiveIntegerField(blank=True, null=True, help_text="Make sure the value is in inches!")
	material_container_made_of = models.CharField(blank=True, null=True, max_length=50)
	
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	slug = models.SlugField(unique=True, blank=True, null=True)

	class Meta(object):
		verbose_name_plural = "Types of Containers"
		ordering = ["-timestamp"]


	@property
	def container_volume(self):
		if self.depth and self.width and self.length:
			return self.depth * self.width * self.length
		return 0

	@property
	def containertype(self):
		if self.material_container_made_of:

			return str(self.container_type_name) + str(self.material_container_made_of)


	def __str__(self):
		return str(self.name) + str(self.container_type_name)

	# def get_absolute_url(self):
	#     return reverse("store:store_details", kwargs={"slug": self.slug})



class Imported(models.Model):
	store = models.ForeignKey(Store, related_name="store_imports")
	supplier_recipt_number = models.BigIntegerField(blank=False, null=False)
	supplier = models.ForeignKey(Supplier, related_name="supplier_imports")
	truck_plate_number = models.CharField(blank=True, null=True, max_length=10)
	product = models.ForeignKey(Products, related_name="product_imports")
	number_of_containers =	models.IntegerField(blank=False, null=False)
	# type_of_containers = models.ForeignKey(ContainersTypes, related_name="contaner_type_imports")
	cost = models.IntegerField(blank=True, null=True)
	price_of_singal_item = models.IntegerField(blank=False, null=False)
	slug = models.SlugField(unique=True, blank=True, null=True)
	date	= models.DateField(auto_now=False, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now = True, auto_now_add=False)
	# payments_done = models.BooleanField(default=False)
	# containers_still_exists = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = "Imports"
		ordering = ["-timestamp"]


	@property
	def total_price(self):
		return self.number_of_containers * self.price_of_singal_item

	@property
	def info(self):
		return str(self.number_of_containers) + " " + str(self.product)  + " " + str(self.imported_date)


	def __str__(self):
			return str(self.product) + " " + str(self.date) + " " + str(self.supplier)


class Exported(models.Model):
	store = models.ForeignKey(Store, related_name="store_exports")
	customer_recipt_number = models.BigIntegerField(blank=True, null=True)
	customer = models.ForeignKey(Customer, related_name="customer_exports")
	truck_plate_number = models.CharField(blank=True, null=True, max_length=10)
	product = models.ForeignKey(Products, related_name="product_exports")
	number_of_containers =	models.IntegerField(blank=False, null=False)
	# type_of_containers = models.ForeignKey(ContainersTypes, related_name="contaner_type_exports")
	cost = models.IntegerField(blank=True, null=True)
	price_of_singal_item = models.IntegerField(blank=False, null=False)
	slug = models.SlugField(unique=True, blank=True, null=True)
	date	= models.DateField(auto_now=False, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now = True, auto_now_add=False)
	# payments_done = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Exports"
		ordering = ["-timestamp"]

	

	@property
	def total_price(self):
		return self.number_of_containers * self.price_of_singal_item

	@property
	def info(self):
		return str(self.number_of_containers) + " " + str(self.product) + " " + str(self.exported_date)

	

	def __str__(self):
			return str(self.product) + " " + str(self.date) + " " + str(self.customer)


class PaymentsOfCustomers(models.Model):
	store = models.ForeignKey(Store, related_name="store_export_payments")
	customer = models.ForeignKey(Customer, related_name="customer_payments")
	payment_method = models.CharField(max_length=50)
	amount = models.IntegerField(blank=False,null=False)
	date = models.DateField(auto_now=False, auto_now_add=False)
	# info_about_payment = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add= True)

	slug = models.SlugField(unique=True, blank=True, null=True)


	class Meta:
		verbose_name_plural = "Payments OF Customers"
		ordering = ["-timestamp"]

	def __str__(self):
		return str(self.customer) + str(self.amount) + str(self.date)


class PaymentsToSuppliers(models.Model):
	store = models.ForeignKey(Store, related_name="store_import_payments")
	supplier = models.ForeignKey(Supplier, related_name="supplier_payments")
	payment_method = models.CharField(max_length=50)
	amount = models.IntegerField(blank = False, null=False)
	date = models.DateField(auto_now=False, auto_now_add=False)
	# info_about_payment = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add= True)

	slug = models.SlugField(unique=True, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Payments To Suppliers"
		ordering = ["-timestamp"]

	def __str__(self):
		return str(self.supplier) + str(self.amount) + str(self.date)


def pre_save_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_slug, sender=Customer)
pre_save.connect(pre_save_slug, sender=Supplier)
pre_save.connect(pre_save_slug, sender=Store)
pre_save.connect(pre_save_slug, sender=Products)
# pre_save.connect(pre_save_slug, sender=ContainersTypes)
pre_save.connect(pre_save_slug, sender=Imported)
pre_save.connect(pre_save_slug, sender=Exported)
pre_save.connect(pre_save_slug, sender=PaymentsOfCustomers)
pre_save.connect(pre_save_slug, sender=PaymentsToSuppliers)
