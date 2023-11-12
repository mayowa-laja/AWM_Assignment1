import json

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from user_location.models import Profile

# Create your views here.


def update_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        retrieved_id = data.get('user_id')
        new_latitude = data.get('lat')
        new_longitude = data.get('lon')

        user_ = User.objects.get(id=int(retrieved_id))
        profile = Profile.objects.get(user=user_)
        profile.lat = new_latitude
        profile.lon = new_longitude
        profile.save()

        return JsonResponse({'message': 'Location updated successfully'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

