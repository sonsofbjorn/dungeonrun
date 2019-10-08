from django.urls import path

from . import web_view

urlpatterns = [
    path('', web_view.index, name='index'),
]
