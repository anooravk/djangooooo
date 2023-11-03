from django.db import models
from django.utils import timezone

statusChoice = (
    ('not started', 'NOT STARTED'),
    ('active', 'ACTIVE'),
    ('on going', 'ON GOING'),
    ('ended', 'ENDED')
)

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=100)
    hostName = models.CharField(max_length=50)
    hostEmail = models.CharField(max_length=50)
    description = models.TextField(null=True)
    location = models.CharField(max_length=100)
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField(default=timezone.now)
    endTime = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=statusChoice, default='not started')
    invitees = models.TextField()  
    attendees = models.TextField()  
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.eventName

