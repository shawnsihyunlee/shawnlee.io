from django.urls import path
from . import views
app_name = 'homepage'

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("about/", views.AboutView, name="about"),
    path("blog/", views.BlogView, name="blog"),
]