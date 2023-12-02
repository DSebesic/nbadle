from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class NBADataView(APIView):
    def get(self, request):
        # Make a request to the NBA API
        api_url = "https://www.balldontlie.io/api/v1/teams"
        response = requests.get(api_url)

        # Return the API response to the client
        return Response(response.json())
