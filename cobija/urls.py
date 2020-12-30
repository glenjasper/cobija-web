"""cobija URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('apps.core.urls', 'core_app'), namespace = 'core_app')),
    path('pet/', include(('apps.pet.urls', 'pet_app'), namespace = 'pet_app')),
    path('partner/', include(('apps.partner.urls', 'partner_app'), namespace = 'partner_app')),
    path('event/', include(('apps.event.urls', 'event_app'), namespace = 'event_app')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Custom titles for admin
admin.site.site_title = "Cobija de  Amor"
admin.site.site_header = "Cobija de Amor"
