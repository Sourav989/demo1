from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied','Applied'),
        ('Interviewing','Interviewing'),
        ('Offered','Offered'),
        ('Rejected','Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company =  models.CharField(max_length = 100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    resume = models.FileField(upload_to = 'resume/',blank=True)
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.position}"
    