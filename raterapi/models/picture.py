from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pictures")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="pictures")
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Picture for {self.game.title}"
