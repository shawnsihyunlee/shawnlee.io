from django.db import models
from datetime import date, timedelta
# Create your models here.

class Workout(models.Model):
    TIME_CHOICES = [
        (10, "10"),
        (20, "20"),
        (30, "30"),
        (40, "40"),
        (50, "50"),
        (60, "60"),
        (70, "70"),
        (80, "80"),
        (90, "90"),
        (100, "100"),
        (110, "110"),
        (120, "120"),
    ]
    MUSCLE_CHOICES = [
        ("chest", "Chest"),
        ("back", "Back"),
        ("legs", "Legs"),
        ("shoulders", "Shoulders"),
        ("biceps", "Biceps"),
        ("triceps", "Triceps"),
        ("abs", "Abs"),
        ("cardio", "Cardio"),
    ]
    workout_date = models.DateField("Workout Date", default=date.today)
    workout_time = models.PositiveIntegerField("Workout Duration", default=60, choices=TIME_CHOICES)
    muscle_group = models.TextField("Muscle Group", choices=MUSCLE_CHOICES)
    
    def __str__(self):
        return ("{date}, {duration} minutes, {group}".format(date=str(self.workout_date), duration=str(self.workout_time), group=str(self.muscle_group).capitalize()))
    
    
class Routine(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    # TODO: Create separate models that inherit from a center Routine class for diff muscle groups
    routine_name = models.CharField("Routine Name", max_length=100)
    num_sets = models.PositiveSmallIntegerField("Number of sets")
    num_reps = models.PositiveSmallIntegerField("Number of reps")
    def __str__(self):
        return("{routine}:{sets}x{reps}".format(routine=str(self.routine_name), sets=self.num_sets, reps=self.num_reps))
