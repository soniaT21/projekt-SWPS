from django.contrib import admin
from .models import Destination

# Rejestracja modelu Destination w panelu administracyjnym
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at')  # Możesz dostosować pola wyświetlane w adminie

admin.site.register(Destination, DestinationAdmin)
