from django.db import models

# Create your models here.
class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date} at {self.venue}"
