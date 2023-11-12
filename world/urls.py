from django.urls import include, path
from .views import pop_query
from .views import pop_query_json

urlpatterns = [
    path("pop_query/", pop_query, name='pop_query'),
    path("pop_query_json/", pop_query_json, name='pop_query_json'),
]
