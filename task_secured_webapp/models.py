from django.db import models
from .choices import TASK_STATUS_OPTIONS, TASK_PRIORITY_OPTIONS #imported options which is used here for dropdown
from django.utils import timezone

# Create your models here.

class TaskCategory(models.Model):

    #task name must be present but description is optional
    cat_name=models.CharField(max_length=100, unique=True)
    cat_desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name
    
class ActualTask(models.Model):
    
    task_title=models.CharField(max_length=255)
    task_description=models.TextField()
    task_due_date=models.DateField()
    task_status=models.CharField(max_length=25, choices=TASK_STATUS_OPTIONS, default="Choose Status")
    task_priority=models.CharField(max_length=25, choices=TASK_PRIORITY_OPTIONS, default="Choose Priority")
    task_category=models.ForeignKey(TaskCategory,on_delete=models.CASCADE)

    
    def if_expired(self):
        if self.task_due_date<timezone.now.date() and self.task_status!='Completed':
            self.task_status='Expired'
            self.save()

    def __str__(self):  
       return self.task_title
    
            

