# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import calculate_stats, sort_stories_by_date


class StatsView(APIView):
    def get(self, request):
        """Fetch calculated statistics."""
        try:
            resin, resout, entries, stories = calculate_stats()
            sorted_stories = sort_stories_by_date(stories)

            # Build response in the same structure as your PHP script
            final_result = []
            for idx, (key, value) in enumerate(resout.items()):
                final_result.append({
                    'id': idx,
                    'hospName': key,
                    'generalRate': value,
                    'rate': resin[key],
                    'stories': sorted_stories[key][0],
                    'numOfVotes': entries[key]
                })
            return Response(final_result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
