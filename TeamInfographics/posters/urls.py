from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nov2019/<int:pk>', views.TeamDetailView.as_view(), name='nov2019-detail'),
]