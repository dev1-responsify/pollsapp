from rest_framework import serializers
from .models import Poll, Choice, Vote

#Serializer to turn all the data into JSON format for the user
class VoteSerializer(serializers.ModelSerializer):
    #class Meta has many attributes but we use this to denote model and what fields to show
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

      