from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.user_home_page, name="home"),
    
    url(r'^admin/', admin.site.urls),
	url(r'^account/', include("account.urls")),
    
    url(r'^store/', include("store.urls", namespace="store")),
    url(r'^company/', include("company.urls", namespace="company")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

