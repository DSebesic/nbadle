import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats    

class PlayerDataView(APIView):
    def get(self, request, player_name):
        players_dict =  players.find_players_by_full_name(player_name)[0]

        print(players_dict)
        return Response(json.dumps(players_dict))

class PlayerCareerStats(APIView):
    def get(self, request, player_id):
        player_career = playercareerstats.PlayerCareerStats(player_id='203999') 

        print(player_career)
        return Response(json.dumps(player_career))
