from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField()

    class Meta:
        unique_together = ("user", "game")

    def __str__(self):
        return f"{self.user} rated {self.game.title}: {self.rating}"
