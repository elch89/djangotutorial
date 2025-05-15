from ..models import Survey
from ..serializers import SurveySerializer

def get_all_surveys():
    surveys = Survey.objects.all()
    return SurveySerializer(surveys, many=True).data