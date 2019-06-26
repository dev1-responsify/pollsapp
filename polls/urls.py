from django.urls import path
from .views import polls_list, polls_detail

#The Routing that calls the polls_list and polls_detail method
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]