from django.forms import ModelForm, ModelChoiceField
from .models import Workout, Routine

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_date', 'workout_time', 'muscle_group']
    
class RoutineForm(ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super(RoutineForm, self).__init__(*args, **kwargs)
    #     self.fields['workout'].widget.attrs['disabled'] = True
    
    class Meta:
        model = Routine
        fields = ['workout', 'routine_name', 'num_sets', 'num_reps']
