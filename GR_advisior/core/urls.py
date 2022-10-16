from django.urls.conf import path
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name="landing"),
    path('game/', game, name="game"),
    path('answer/', answer, name='answer'),
    path('result/', result, name="result"),
    path('success/', success, name="success"),
]
