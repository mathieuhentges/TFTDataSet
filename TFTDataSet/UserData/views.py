from rest_framework.views import APIView
from rest_framework.response import Response
from riotwatcher import TftWatcher

from TFTDataSet.settings import env


class UsersView(APIView):
    """
    View to list my users in the system.
    """

    def importMatch(self, request, format=None):
        """
        Return a list of all mattch for a user users.
        """

        secret_key = env('RIOT_API_KEY')
        matches = TftWatcher.match.by_puuid(region="na1",
                                            puuid="B6P0NI8Tarrc6cfbH8328cz0m0MsvgtjXq2r_76CLaMAfWzB3U9k2Ekm87EBZFHuLpimQ0rLoE4peg",
                                            count=50)
        return Response(matches)
