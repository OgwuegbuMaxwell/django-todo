from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    # auto_now_add is good for one time creation
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now is good for when you want to be updating the field
    updated_at = models.DateTimeField(auto_now=True)
    
    # String representation of the model
    def __str__(self):
        return self.task
