from django.contrib import admin
from .models import MyPdi

class ListMyPdi(admin.ModelAdmin):
    list_display = ('mypdi_id', 'mypdi_host', 'mypdi_guest', 'mypdi_area', 'mypdi_office', 'mypdi_date_admission', 'mypdi_strong_points', 'mypdi_dev_points', 'mypdi_action_1', 'mypdi_action_time_1', 'mypdi_action_type_1', 'mypdi_status_1', 'mypdi_action_2', 'mypdi_action_time_2', 'mypdi_action_type_2', 'mypdi_status_2', 'mypdi_action_3', 'mypdi_action_time_3', 'mypdi_action_type_3', 'mypdi_status_3', 'mypdi_action_4', 'mypdi_action_time_4', 'mypdi_action_type_4', 'mypdi_status_4', 'mypdi_action_5', 'mypdi_action_time_5', 'mypdi_action_type_5', 'mypdi_status_5', 'mypdi_action_6', 'mypdi_action_time_6', 'mypdi_action_type_6', 'mypdi_status_6', 'mypdi_action_7', 'mypdi_action_time_7', 'mypdi_action_type_7', 'mypdi_status_7', 'mypdi_action_8', 'mypdi_action_time_8', 'mypdi_action_type_8', 'mypdi_status_8', 'mypdi_action_9', 'mypdi_action_time_9', 'mypdi_action_type_9', 'mypdi_status_9', 'mypdi_action_10', 'mypdi_action_time_10', 'mypdi_action_type_10', 'mypdi_status_10', 'mypdi_status_gobal', 'mypdi_main_goal', 'mypdi_cad_hour', )

admin.site.register(MyPdi, ListMyPdi)


