"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import urls as pages_url
from listings import urls as listings_url
from realtors import urls as realtors_url
from accounts import urls as accounts_url
from contacts import urls as contacts_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(pages_url)),
    path("listings/", include(listings_url)),
    path("accounts/", include(accounts_url)),
    path("contacts/", include(contacts_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
