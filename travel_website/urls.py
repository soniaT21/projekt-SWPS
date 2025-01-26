from django.contrib import admin
from django.urls import include, path
from travel.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/', include ('travel.urls')),  
    path('', home),  
]