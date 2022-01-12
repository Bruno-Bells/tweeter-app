from datetime import datetime, time
from django.shortcuts import render
from django.http import JsonResponse
from api.models import Handle, Interval, Tweet
import json, requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer, HandleSerializer, IntervalSerializer
from dateutil import parser
from datetime import datetime

def last_n_hours(num):
    time_diff = num
    today = datetime.now() 
    date = today.date()
    since_hour = max(0, today.hour - time_diff)
    minute = today.minute
    second = '00'
    since_date_str = '%s %s:%s:%s' % (date, since_hour, minute, second)
    
    return since_date_str

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/tweet-list/',
        'Create':'/tweet-create/',
        'Delete':'/tweet-delete/',

        'ListUsername': '/handle-list/',

    }
    return Response(api_urls)

@api_view(['GET'])
def tweetList(request):

    get_interval = requests.get('http://localhost:8000/api/interval/')
    get_interval = get_interval.json()

    interval = int(get_interval['interval'])

    time_interval = last_n_hours(interval)
    time_interval = parser.parse(time_interval)

    tweets = Tweet.objects.filter(created__gt=time_interval)
    print(tweets)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def tweetCreate(request):
    serializer = TweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['DELETE'])
def tweetDelete(request):
    # tweet = Tweet.objects.get(id=interval)
    # tweet.delete()

    return Response("Item Successfully delete!")


@api_view(['GET'])
def handleList(request):
    handle = Handle.objects.all()
    serializer = HandleSerializer(handle, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def intervalList(request):
    interval = Interval.objects.all().last()
    serializer = IntervalSerializer(interval, many=False)
    return Response(serializer.data)