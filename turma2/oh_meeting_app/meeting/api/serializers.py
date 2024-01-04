from rest_framework import serializers
from meeting.models import MyMeeting

class MyMeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyMeeting
        fields = ['mymeeting_id', 'mymeeting_host', 'mymeeting_guest', 'mymeeting_title', 'mymeeting_desc', 'mymeeting_place', 'mymeeting_link', 'mymeeting_room', 'mymeeting_status', 'mymeeting_date', 'mymeeting_hour']