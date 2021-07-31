from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Workout
from .forms import WorkoutForm
# Create your views here.

def HomeView(request):
    recent_workout_list = Workout.objects.order_by('-workout_date')[:5]
    return render(request, 'Tracker/home.html', {'recent_workout_list':recent_workout_list})

def AddWorkoutView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkoutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Tracker:home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm()

    return render(request, 'Tracker/add_workout.html', {'form': form})

def EditWorkoutView(request, workout_id):
    # if this is a POST request we need to process the form data
    instance=Workout.objects.get(pk=workout_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkoutForm(request.POST, instance=instance)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Tracker:home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm(instance=instance)

    return render(request, 'Tracker/edit_workout.html', {'form': form, 'workout_id':workout_id})