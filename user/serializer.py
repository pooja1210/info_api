from rest_framework import routers, serializers, viewsets, fields
from . models import User, ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):
    # start_time = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = ActivityPeriod
        fields = [ 'start_time', 'end_time']
        read_only_fields = ('user_id',)

        

class UserSerializer(serializers.ModelSerializer):
    activity_period = ActivitySerializer(many=True)
    
    class Meta:
        model = User
        fields = ['user_id', 'real_name', 'address', 'activity_period']

    def create(self, validated_data):
        tracks_data = validated_data.pop('activity_period')
        user_id = User.objects.create(**validated_data)
        for track_data in tracks_data:
            ActivityPeriod.objects.create(user_id=user_id, **track_data)
        return user_id

