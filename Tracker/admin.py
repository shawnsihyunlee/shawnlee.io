from django.contrib import admin

# Register your models here.
from .models import Workout, Routine

admin.site.register(Workout)
admin.site.register(Routine)
