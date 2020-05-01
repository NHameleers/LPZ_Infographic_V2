from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nov2019/team/<int:pk>', views.TeamDetailView.as_view(), name='nov2019-team-detail'),
    path('nov2019/locatie/<int:pk>', views.LocatieDetailView.as_view(), name='nov2019-locatie-detail'),
    path('nov2019/organisatie/<int:pk>', views.OrganisatieDetailView.as_view(), name='nov2019-organisatie-detail'),

]