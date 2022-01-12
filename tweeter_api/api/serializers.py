from django.db import models
from rest_framework import serializers
from .models import Tweet, Handle, Interval
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status


# class TweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tweet
#         fields = '__all__'
#         depth = 1

class TweetSerializer(serializers.Serializer):
    data = serializers.JSONField()  # A nested list of 'edit' items.
    status = serializers.BooleanField()
    message = serializers.CharField(max_length=200)
    created = serializers.DateTimeField('date created', default=timezone.now)

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)


class HandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handle
        fields = '__all__'


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interval
        fields = '__all__'