from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Favorite(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100)
    menu = models.CharField(max_length=500)
    hours = models.CharField(max_length=500)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Favorite)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants_detail', kwargs={'pk': self.id})


class Review(models.Model):
    content = models.CharField(max_length=250)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restaurant} has a rating {self.rating} with review: {self.content}"
