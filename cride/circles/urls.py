

# Django
from django.urls import path

# views
from cride.circles.views import list_circles


ulr_patterns = [
    path('/', list_circles)
    ]
