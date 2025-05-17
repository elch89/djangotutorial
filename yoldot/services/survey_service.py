from datetime import datetime
import json
import os
from django.conf import settings

from ..models import Survey
from ..serializers import SurveySerializer

def get_all_surveys():
    surveys = Survey.objects.all()
    return SurveySerializer(surveys, many=True).data


def save_temp_json(data, filename=None):
    if not filename:
        filename = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    
    file_path = os.path.join(settings.TEMP_DIR, filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return file_path