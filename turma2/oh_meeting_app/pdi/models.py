from django.db import models
from datetime import datetime

class MyPdi(models.Model):

    STATUS_CHOICES =  [
        ('AG', 'Aguardando'),
        ('IN', 'Iniciada'),
        ('FI', 'Finalizada'),
    ]

    ACTION_TYPE_CHOICES =  [
        ( '10', 'Formal training'),
        ( '20', 'Co-workers'),
        ( '70', 'On-the-job'),
    ]

    ACTION_TIME_CHOICES =  [
        ( 'ST', 'Curto Prazo'),
        ( 'MD', 'Medio Prazo'),
        ( 'LG', 'Longo Prazo'),
    ]

    mypdi_id = models.BigAutoField(primary_key=True)
    mypdi_host = models.CharField(max_length=100)
    mypdi_guest = models.CharField(max_length=100)
    mypdi_area = models.CharField(max_length=100)
    mypdi_office = models.CharField(max_length=300)
    mypdi_date_admission = models.DateField(blank=True)
    mypdi_strong_points = models.CharField(max_length=300)
    mypdi_dev_points = models.CharField(max_length=300)
    
    mypdi_action_1 = models.CharField(max_length=100)
    mypdi_action_time_1 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_1= models.CharField(max_length=100)
    mypdi_status_1 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_2 = models.CharField(max_length=100)
    mypdi_action_time_2 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_2 = models.CharField(max_length=100)
    mypdi_status_2 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_3 = models.CharField(max_length=100)
    mypdi_action_time_3 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_3 = models.CharField(max_length=100)
    mypdi_status_3 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_4 = models.CharField(max_length=100)
    mypdi_action_time_4 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_4 = models.CharField(max_length=100)
    mypdi_status_4 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_5 = models.CharField(max_length=100)
    mypdi_action_time_5 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_5 = models.CharField(max_length=100)
    mypdi_status_5 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_6 = models.CharField(max_length=100)
    mypdi_action_time_6 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_6 = models.CharField(max_length=100)
    mypdi_status_6 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_7 = models.CharField(max_length=100)
    mypdi_action_time_7 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_7 = models.CharField(max_length=100)
    mypdi_status_7 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_8 = models.CharField(max_length=100)
    mypdi_action_time_8 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_8 = models.CharField(max_length=100)
    mypdi_status_8 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_9 = models.CharField(max_length=100)
    mypdi_action_time_9 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_9 = models.CharField(max_length=100)
    mypdi_status_9 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_action_10 = models.CharField(max_length=100)
    mypdi_action_time_10 = models.CharField(max_length=2, choices=ACTION_TIME_CHOICES)
    mypdi_action_type_10 = models.CharField(max_length=100)
    mypdi_status_10 = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    mypdi_status_gobal = models.CharField(max_length=2, choices=STATUS_CHOICES)
    mypdi_main_goal = models.CharField(max_length=150)
    mypdi_cad_hour = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (self.mypdi_host, self.mypdi_guest)