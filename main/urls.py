# main/urls.py

# main/urls.py

from django.urls import path
from .views import login_view, dashboard_view

urlpatterns = [
    path('', login_view, name='login'),           # URL for login page
    path('dashboard/', dashboard_view, name='dashboard') # URL for dashboard page
]
