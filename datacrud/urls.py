from django.urls import path

from . import views


urlpatterns = [
    path('data', views.DataCreateView.as_view()),
    path('data/<int:pk>', views.DataRetrieveView.as_view()),
]