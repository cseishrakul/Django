from django.db import models
from django.urls import reverse
# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('view_url_app:musician_detail', kwargs={'pk': self.pk})


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    rating = (
        (1, "Worst"),
        (2, "ok"),
        (3, "nice"),
        (4, "Like"),
        (5, "Wow"),
    )

    num_starts = models.IntegerField(choices=rating)

    def __str__(self):
        return "Name: " + self.name + ", Rating: " + str(self.num_starts)
