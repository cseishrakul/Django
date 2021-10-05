from django.conf.urls import url
from django.urls import path
from view_url_app import views

app_name = "view_url_app"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('musician_detail/<pk>/', views.MusicianDetail.as_view(), name="musician_detail"),
    path('add_musician/', views.AddMusician.as_view(), name="add_musician"),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name="musician_update"),
    path('musician_delete/<pk>/', views.DeleteMusician.as_view(), name="musician_delete"),
]
