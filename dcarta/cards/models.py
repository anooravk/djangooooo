from django.db import models


class BusniessCards(models.Model):
    cardId = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=50)
    companyName = models.TextField(null=True)
    address = models.TextField(null=True)
    jobTitle = models.CharField(max_length=100)
    exchangers = models.TextField(default='')  
   
    def __str__(self):
        return self.companyName

