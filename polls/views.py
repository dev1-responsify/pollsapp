from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll
# Create your views here.

#Function that sends a request
def polls_list(request):
    MAX_OBJECTS = 20 #initialize the max objects to return in an integer
    polls = Poll.objects.all()[:MAX_OBJECTS] #Make a list that goes up the MAX_OBJECTS and put all the poll objects.
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))} #Make a key called results and attach the list from the DB
    return JsonResponse(data) #return a JSON response from the data variable


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)