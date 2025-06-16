
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("inventory.urls"))
]

if settings.DEBUG:
    urlpatterns+= [path("__debug__/", include("django_browser_reload.urls"))]