from django.urls import path

from weather import views
from weather.api import views as apiviews



urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
    path('api/v1/statistics/regions/', apiviews.RegionView.as_view(), name='regions_statistics'),
]