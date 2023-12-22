from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Update the URL pattern for the root URL
    path('<str:month>/', views.monthlyChallenges, name='month-challenge'),
    path('<int:month>/', views.numbers),
]
