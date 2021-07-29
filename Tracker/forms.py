from django.forms import ModelForm
from .models import Workout, Routine

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_date', 'workout_time', 'muscle_group']
    
    