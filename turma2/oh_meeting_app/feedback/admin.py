from django.contrib import admin
from .models import MyFeedback

class ListMyFeedback(admin.ModelAdmin):
    list_display = ('myfeedback_id', 'myfeedback_meeting_id', 'myfeedback_host', 'myfeedback_guest', 'myfeedback_question1', 'myfeedback_answer1', 'myfeedback_question2', 'myfeedback_answer2', 'myfeedback_question3', 'myfeedback_answer3', 'myfeedback_classification', 'myfeedback_cad_hour')

admin.site.register(MyFeedback, ListMyFeedback)

