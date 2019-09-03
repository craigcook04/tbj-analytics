from django.db import models

# Create your models here.

class Player(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    # playerId = models.CharField(max_length=100)
    # def __str__(self):
    #     return self.firstName, self.lastName

class Team(models.Model):
    teamId = models.CharField(max_length=100)
    teamName = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.teamName, self.venue, self.division
