from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    player_count = models.IntegerField()
    completion_hours = models.IntegerField()
    recommended_age = models.IntegerField()
    categories = models.ManyToManyField("Category", related_name="games", blank=True)

    def __str__(self):
        return f"Game: {self.title}"
