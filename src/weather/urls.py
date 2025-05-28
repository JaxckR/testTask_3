from django.urls import path

from weather import views



urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
]