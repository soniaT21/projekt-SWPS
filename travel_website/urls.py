from django.contrib import admin
from django.urls import include, path
from travel.views import home, add_trip, login_view  # Importowanie widoków

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/', include('travel.urls')),  
    path('', home, name='home'),  # Strona główna
    path('login/', login_view, name='login'),  # Logowanie
    path('add_trip/', add_trip, name='add_trip'),  # Dodaj podróż
]
