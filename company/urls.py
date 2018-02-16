from django.conf.urls import url, include

from . import views

app_name = "company"


urlpatterns = [
    url(r'^add-company$', views.CompanyCreateView.as_view(), name="add_company"),

    url(r'^(?P<company_slug>[\w-]+)/add-store/$', views.StoreCreateView.as_view(), name="add_store"),
    url(r'^(?P<company_slug>[\w-]+)/stores-list/$', views.StoresListView.as_view(), name="stores-list"),
    url(r'^companies-list/$', views.CompaniesListView.as_view(), name="list_companies"),
    url(r'^(?P<company_slug>[\w-]+)/company-details$', views.CompanyDetailView.as_view(), name="company_details"),
    url(r'^(?P<company_slug>[\w-]+)/update-company$', views.CompanyUpdateView.as_view(), name="update_company"),
    url(r'^(?P<company_slug>[\w-]+)/delete-company$', views.company_delete_view, name="delete_company"),

]
