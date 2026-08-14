from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=(('male', 'male'), ('female', 'female')), blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


