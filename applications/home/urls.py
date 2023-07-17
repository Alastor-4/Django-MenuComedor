from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('menu/', views.HomePageView.as_view(), name='home-menu',),
]