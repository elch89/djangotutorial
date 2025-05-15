from django.urls import path

from yoldot.views import UserView
from yoldot.views import HashvaaView
from yoldot.views import StatsView
from yoldot.views import SurveyView

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<email>/', UserView.as_view(), name='user-detail'),
    path('hashvaa/', HashvaaView.as_view(), name='hashvaa-list'),
    path('survey/', SurveyView.as_view(), name = 'survey-list'),
    path('stats/', StatsView.as_view(), name='stats-calculation')
]