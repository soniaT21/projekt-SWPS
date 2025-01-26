from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Review, Traveler, Trip
from .forms import DestinationForm, ReviewForm, TripForm # type: ignore

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'travel/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'travel/destination_detail.html', {'destination': destination})

def destination_edit(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_detail', pk=destination.pk)
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'travel/destination_edit.html', {'form': form})

def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        destination.delete()
        return redirect('destination_list')
    return render(request, 'travel/destination_confirm_delete.html', {'destination': destination})

def traveler_trip_summary(request):
    travelers = Traveler.objects.prefetch_related('trips').all()
    return render(request, 'travel/traveler_trip_summary.html', {'travelers': travelers})

def destination_reviews(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    reviews = destination.reviews.all()
    return render(request, 'travel/destination_reviews.html', {'destination': destination, 'reviews': reviews})
def home(request):
    return HttpResponse("Welcome to the Travel Website!")
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
