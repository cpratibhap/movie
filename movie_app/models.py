from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_name = models.CharField(max_length=50, null=False)
    actor = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "{} - {}".format(self.movie_name, self.actor)

