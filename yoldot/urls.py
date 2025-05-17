from django.urls import path

from yoldot.views import (
    UserView,
    HashvaaView,
    StatsView,
    SurveyView,
    CouponDetailView,CouponListView,
    CourseDetailView,LessonDetailView,LessonListView,CourseListView,
    AppVersionView
    )

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<email>/', UserView.as_view(), name='user-detail'),
    path('hashvaa/', HashvaaView.as_view(), name='hashvaa-list'),
    path('survey/', SurveyView.as_view(), name = 'survey-list'),
    path('stats/', StatsView.as_view(), name='stats-calculation'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
     # Courses
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<str:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Lessons
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<str:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    
    path('app-versions/', AppVersionView.as_view(), name='app-version-list'),
    path('app-versions/<str:platform>/', AppVersionView.as_view(), name='app-version-detail'),
    # path('',PodcastView.as_view(), name='podcats-list')
]