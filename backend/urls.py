from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
]
