from django.db import models

# Create your models here.
class Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=30)
    no_matches = models.FloatField()
    def __str__(self):
        return f"{self.playerid} - {self.playername} - {self.no_matches}"