from django.urls import path
from Log_In.views import *

urlpatterns = [
    path('signin_view/', signin_view, name="signin_view"),
    path('qa_vark/', qa_vark, name="qa_vark"),
    path('qa_hobbies/', qa_hobbies, name="qa_hobbies"),
]