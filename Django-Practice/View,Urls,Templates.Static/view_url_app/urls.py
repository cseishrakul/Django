from django.conf.urls import url
from django.urls import path
from view_url_app import views

urlpatterns = [
    path('', views.index, name="home"),
]
