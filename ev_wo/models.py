from platform import mac_ver
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class org(models.Model):
    organiser_name = models.CharField(max_length=30,unique=True)
    organiser_email = models.EmailField()
    organiser_no = models.CharField(max_length=10,unique=True)

class events(models.Model):
    ids = (('DA','department'),('CB','club'))
    event_id = models.CharField(max_length=4,choices=ids)
    event_name = models.CharField(max_length=30,unique=True)
    event_organiser = models.CharField(max_length=30,null =False, blank=False)
    event_description = models.CharField(max_length=150,null =False, blank=False)
    event_poster = models.ImageField(upload_to='images')
    org = models.ForeignKey('org',default=1,on_delete=models.CASCADE)
    registration_link = models.URLField(max_length=200)