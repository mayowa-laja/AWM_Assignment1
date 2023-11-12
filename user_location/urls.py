from django.urls import include, path
from .views import update_location

urlpatterns = [
    path("update_location/", update_location, name='update_location'),
]
