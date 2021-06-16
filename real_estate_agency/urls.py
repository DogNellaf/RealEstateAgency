from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^grappelli/', include('grappelli.urls')),
    path('', include('estate.urls'))
]
