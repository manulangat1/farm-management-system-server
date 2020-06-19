from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('backend.urls')),
    path('ap/',include('backend.s_urls'))
]
