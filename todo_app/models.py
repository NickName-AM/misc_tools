from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    heading = models.CharField(max_length=30, help_text="Keep it brief.")
    description = models.CharField(max_length=100, help_text="Full Description(OR short).")
    date_added = models.DateField(auto_now_add=True)
    noteuser = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.heading