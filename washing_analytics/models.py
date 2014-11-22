from django.db.models.fields.related import ManyToManyField
import hashlib
import random
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


EventTypeChoice = (
    (0, 'Wash'),
    (1, 'WiiBoard')
)

class GUIDModel(models.Model):
    guid = models.CharField(primary_key=True, max_length=40)

    def save(self, *args, **kwargs):
        if not self.guid:
            self.guid = hashlib.sha1(str(random.random())).hexdigest()

        super(GUIDModel, self).save(*args, **kwargs)


# Create your models here.
class Event(GUIDModel):
    date = models.DateTimeField(blank=False, default=datetime.now())
    duration = models.FloatField(blank=False, default=0.0)
    status = models.CharField(max_length=1, choices=EventTypeChoice)



class Division(models.Model):
    name = models.CharField(max_length=512, blank=False)
    description = models.CharField(max_length=2048, blank=False)


class Team(models.Model):
    name = models.CharField(max_length=512, blank=False)
    description = models.CharField(max_length=2048, blank=False)

    division = models.ForeignKey(Division)


class Account(models.Model):
    name = models.CharField(max_length=512, blank=False)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lng = models.FloatField(blank=True, null=True)

    teams = ManyToManyField(Team, through='Membership')


class Membership(models.Model):
    team = models.ForeignKey(Team)
    account = models.ForeignKey(Account)


class TeamReduce(models.Model):
    team = models.ForeignKey(Team)
    division = models.ForeignKey(Division)
    complete = models.IntegerField(blank=False, null=False)
    washed = models.IntegerField(blank=False, null=False)
    unwashed = models.IntegerField(blank=False, null=False)
    timespent = models.FloatField(blank=False, null=False)
