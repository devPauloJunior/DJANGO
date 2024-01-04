from django.contrib import admin
from .models import MyMeeting

class ListMyMeeting(admin.ModelAdmin):
    list_display = ('mymeeting_id', 'mymeeting_host', 'mymeeting_guest', 'mymeeting_title', 'mymeeting_desc', 'mymeeting_place', 'mymeeting_link', 'mymeeting_room', 'mymeeting_status', 'mymeeting_date', 'mymeeting_hour')

admin.site.register(MyMeeting, ListMyMeeting)
