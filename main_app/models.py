from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    menu = models.CharField(max_length=500)
    hours = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('restaurants_detail', kwargs={'pk': self.id})
        # return reverse('restaurants_detail', kwargs={'restaurant_id': self.id})
    