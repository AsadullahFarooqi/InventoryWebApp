from django.conf.urls import url

from . import views

app_name = "store"


urlpatterns = [
    url(r'^(?P<store_slug>[\w-]+)/Dashboard/$', views.dashboard, name="dashboard"),

    ############## CREATE VIEWS  ******************
    
    url(r'^(?P<store_slug>[\w-]+)/add-employer/$', views.EmployerCreateView.as_view(), name="add_employer"),
    url(r'^(?P<store_slug>[\w-]+)/add-customer/$', views.CustomerCreateView.as_view(), name="add_customer"),
    url(r'^(?P<store_slug>[\w-]+)/add-supplier/$', views.SupplierCreateView.as_view(), name="add_supplier"),
    url(r'^(?P<store_slug>[\w-]+)/add-product/$', views.ProductsCreateView.as_view(), name="add_product"),
    # url(r'^(?P<store_slug>[\w-]+)/add-container-type/$', views.ContainerTypesCreateView.as_view(), name="add_container_type"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/add-import/$', views.ImportCreateView.as_view(), name="add_import"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/add-export/$', views.ExportCreateView.as_view(), name="add_export"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/add-customer-payments/$', views.CustomerPaymentCreateView.as_view(), name="add_customer_payment"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/add-supplier-payments/$', views.SupplierPaymentCreateView.as_view(), name="add_supplier_payment"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/add-employer-payments/$', views.EmployersLedgerCreateView.as_view(), name="add_employer_payment"),

    ############## LIST VIEWS  ******************

    url(r'^(?P<store_slug>[\w-]+)/employers-list/$', views.employers_list_view, name="employers_list"),
    url(r'^(?P<store_slug>[\w-]+)/suppliers-list/$', views.supplier_list_view, name="suppliers_list"),
    url(r'^(?P<store_slug>[\w-]+)/customers-list/$', views.customer_list_view, name="customers_list"),

    url(r'^(?P<supplier_slug>[\w-]+)/(?P<sup_product>[\w]+[\s\w]+)/$', views.supplier_product_imports_list, name="supplier_product"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/(?P<cus_product>[\w]+[\s\w]+)/$', views.customer_product_imports_list, name="customer_product"),

    url(r'^(?P<store_slug>[\w-]+)/products-list/$', views.ProductsListView.as_view(), name="products_list"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<date>(\d+.\d+.\d+))/day-reports/$', views.day_report_by_date, name="day_report_by_date"),

    url(r'^(?P<store_slug>[\w-]+)/imports-list/$', views.ImportedListView.as_view(), name="imports_list"),
    url(r'^(?P<store_slug>[\w-]+)/exports-list/$', views.ExportedListView.as_view(), name="exports_list"),

    url(r'^(?P<store_slug>[\w-]+)/export-payments-list/$', views.CustomerPaymentsListView.as_view(), name="export_payments_list"),
    url(r'^(?P<store_slug>[\w-]+)/import-payments-list/$', views.SupplierPaymentsListView.as_view(), name="import_payments_list"),

    url(r'^(?P<store_slug>[\w-]+)/employers-payments-list/$', views.EmployerPaymentsListView.as_view(), name="employers_payments_list"),

    ############## DETAIL VIEWS ******************

    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/employer-details/$', views.employer_profile_view, name="employer_profile"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/customer-details/$', views.customer_profile_view, name="customer_profile"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/supplier-details/$', views.supplier_profile_view, name="supplier_profile"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<import_slug>[\w-]+)/import-details/$', views.import_details_view, name="import_details"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<export_slug>[\w-]+)/export-details/$', views.export_details_view, name="export_details"),


    ############## UPDATE VIEWS  ******************
    
    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/update-employer/$', views.EmployerUpdateView.as_view(), name="update_employer"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/update-customer/$', views.CustomerUpdateView.as_view(), name="update_customer"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/update-supplier/$', views.SupplierUpdateView.as_view(), name="update_supplier"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<product_slug>[\w-]+)/update-product/$', views.ProductsUpdateView.as_view(), name="update_product"),
    # url(r'^(?P<store_slug>[\w-]+)/(?P<container_type_slug>[\w-]+)/update-container-type/$', views.ContainerTypesUpdateView.as_view(), name="update_container_type"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/(?P<import_slug>[\w-]+)/update-import/$', views.ImportUpdateView.as_view(), name="update_import"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/(?P<export_slug>[\w-]+)/update-export/$', views.ExportUpdateView.as_view(), name="update_export"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/update-customer-payment/$', views.CustomerPaymentUpdateView.as_view(), name="update_customer_payment"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/update-supplier-payment/$', views.SupplierPaymentUpdateView.as_view(), name="update_supplier_payment"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/update-employer-payment/$', views.EmployerPaymentUpdateView.as_view(), name="update_employer_payment"),

    ############## DELETE VIEWS  ******************
    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/delete-employer/$', views.employer_delete_view, name="delete_employer"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/delete-customer/$', views.customer_delete_view, name="delete_customer"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/delete-supplier/$', views.supplier_delete_view, name="delete_supplier"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<product_slug>[\w-]+)/delete-product/$', views.products_delete_view, name="delete_product"),
    # url(r'^(?P<store_slug>[\w-]+)/(?P<container_type_slug>[\w-]+)/delete-container-type/$', views.container_type_delete_view, name="delete_container_type"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<import_slug>[\w-]+)/delete-import/$', views.import_delete_view, name="delete_import"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<import_slug>[\w-]+)/delete-export/$', views.export_delete_view, name="delete_export"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<customer_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/delete-customer-payment/$', views.customer_payment_delete_view, name="delete_customer_payment"),
    url(r'^(?P<store_slug>[\w-]+)/(?P<supplier_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/delete-supplier-payment/$', views.supplier_payment_delete_view, name="delete_supplier_payment"),

    url(r'^(?P<store_slug>[\w-]+)/(?P<employer_slug>[\w-]+)/(?P<payment_slug>[\w-]+)/delete-employer-payment/$', views.employer_payment_delete_view, name="delete_employer_payment"),

]
