from django.contrib import admin
from django.urls import path
from work.V1.auth import Sign_in, Sign_up
from work.V1.core import ExperienceView
from work.V1.post import PostViewOne, PostView


urlpatterns = [

    path('linkedIn/sign-in/', Sign_in.as_view()),
    path('linkedIn/sign-up/', Sign_up.as_view()),
    # post
    path('linkedIn/post/', PostViewOne.as_view()),
    path('linkedIn/<int:pk>/', PostViewOne.as_view()),
    # post many
    path('linkedIn/post/', PostView.as_view()),
    path('linkedIn/<int:pk>/', PostView.as_view()),
    # experience
    path('linkedIn/exp/', ExperienceView.as_view()),
    path('linkedIn/<int:pk>/', PostViewOne.as_view()),

]
