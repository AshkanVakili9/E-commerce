from django.urls import path
from .views import *


urlpatterns = [

    # product views
    path('index/', index, name='index'),

]
