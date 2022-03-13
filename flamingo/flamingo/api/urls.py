from django.urls import path
from .views import *

app_name = "api"

urlpatterns = [
    path('',home ,name='home'),
    path('insert/', insert, name="insert"),
    path('graph/', graph, name="graph"),
]