from django.urls import path
from mumbai.views import *
app_name='mumbai'
urlpatterns=[
    path('rohith/',rohith,name='rohith'),
]