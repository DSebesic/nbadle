from django.urls import path
from .views import NBADataView

urlpatterns = [
    path('nba-data/', NBADataView.as_view(), name='nba-data'),
]
