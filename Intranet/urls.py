from django.urls import path
from Intranet.views import *

urlpatterns = [
    path('search/', search, name="search"),
    path('profile/', profile, name="profile"),
    path('mylearning/', mylearning, name="mylearning"),
    path('subject/<int:code>/', subject, name="subject"),
    path('enroll_subject/<int:code>/', enroll_subject, name="enroll_subject"),
    path('lesson/<int:code>/', lesson, name="lesson"),
    path('test_evaluation/<int:code>/', test_evaluation, name="test_evaluation"),
    path('logout_view/', logout_view, name="logout_view"),
]