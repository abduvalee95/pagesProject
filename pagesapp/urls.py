from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about-us'),

    path('', HomePageView.as_view(),name='home'),
]

