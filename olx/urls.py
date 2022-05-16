from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
]
