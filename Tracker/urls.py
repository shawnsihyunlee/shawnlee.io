from django.urls import path
from . import views
app_name = 'Tracker'
urlpatterns = [
    path('', views.HomeView, name="home"),
    path('add/', views.AddWorkoutView, name="add_workout"),
    path('edit/<int:workout_id>/', views.EditWorkoutView, name="edit_workout"),
    path('addroutine/<int:workout_id>/', views.AddRoutineView, name="add_routine"),
    path('deleteroutine/<int:routine_id>/', views.DeleteRoutineView, name="delete_routine"),
]