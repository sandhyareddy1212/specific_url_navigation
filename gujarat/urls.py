from django.urls import path
from gujarat.views import *
app_name='gujarat'
urlpatterns=[
    path('hardik/',hardik,name='hardik'),
]