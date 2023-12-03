from django.urls import path
from .views import PlayerCareerStats, PlayerDataView

urlpatterns = [
    path('player-data/<str:player_name>', PlayerDataView.as_view(), name='player-data'),
    path('player-stats/<int:player_id>', PlayerCareerStats.as_view(), name='player-stats'),
]
