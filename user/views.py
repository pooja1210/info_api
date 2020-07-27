from django.shortcuts import render
from .models import User, ActivityPeriod
from rest_framework import viewsets
from.serializer import UserSerializer, ActivitySerializer
from rest_framework.decorators import action

# Create your views here.


def user_list(request):
    user = User.objects.all()
    activity_dict = {}
    activity = ActivityPeriod.objects.all()
    
    # for i in activity:
    #     activity_dict[i.user_id] = i.start_time
    context = {
        "user": user,
        # "activity": activity,
        "my_dict":activity_dict
    }
    
    return render(request,'list.html',context)
from django.http import JsonResponse
def activityPeriod(request):
    user_id =request.GET.get('user_id')
    acti_list =[]
    activity = ActivityPeriod.objects.filter(user_id=user_id).values('start_time','end_time')
    for acti in activity:
        acti_list.append({'start_time':acti['start_time'].strftime('%b %d %Y  %I:%M%p'),'end_time':acti['end_time'].strftime('%b %d %Y  %I:%M%p')})
        # acti_list.append({'start_time':acti['start_time'],'end_time':acti['end_time']})
    return JsonResponse(acti_list,safe=False)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    