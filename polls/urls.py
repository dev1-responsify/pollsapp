from django.urls import path
from .apiviews import PollList, PollDetail

#The Routing that calls the polls_list and polls_detail method
urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]