from rest_framework import serializers
from pdi.models import MyPdi

class MyPdiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyPdi
        fields = ['mypdi_id', 'mypdi_host', 'mypdi_guest', 'mypdi_area', 'mypdi_office', 'mypdi_admission', 'mypdi_obj_short_term', 'mypdi_obj_short_date', 'mypdi_obj_mid_term', 'mypdi_obj_mid_date', 'mypdi_obj_long_term', 'mypdi_obj_long_date', 'mypdi_obj_strong_points', 'mypdi_obj_dev_points', 'mypdi_action70', 'mypdi_status70', 'mypdi_action20', 'mypdi_status20', 'mypdi_action10', 'mypdi_status10', 'mypdi_status_gobal', 'mypdi_main_goal', 'mypdi_cad_hour']