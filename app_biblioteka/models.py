from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=32)

    def __str__(self):
        return self.name, self.author


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
