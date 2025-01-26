# travel/forms.py
from django import forms
from .models import Destination, Review, Trip  # Zależnie od twoich modeli

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['destination', 'rating', 'comment']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'start_date', 'end_date']

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip  
        fields = ['destination', 'start_date', 'end_date', 'rating']
          
