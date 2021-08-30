from django.conf.urls import url
from django.urls import path
from view_url_app import views

app_name = "view_url_app"

urlpatterns = [
    path('', views.index, name="home"),
    path('form/', views.form, name="form"),
]
