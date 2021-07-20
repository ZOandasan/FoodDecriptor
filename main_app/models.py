from django.db import models
from django.urls import reverse

# Create your models here.
RATINGS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

TASTE = (
    ('SWEET', 'Sweet'),
    ('SOUR', 'Sour'),
    ('SALTY', 'Salty'),
    ('BITTER', 'Bitter'),
    ('SAVORY', 'Savory')
)

class Side(models.Model):
    name = models.CharField(max_length=50)
    taste = models.CharField(
        "taste",
        max_length=7,
        choices=TASTE,
        default=TASTE[0][0]
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('side_detail', kwargs={'pk': self.id})


class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    meal = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    sides = models.ManyToManyField(Side)

    def __str__(self):
        return f"{self.name} is {self.meal}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})



class Review(models.Model):
    content = models.CharField(max_length=500)
    rating = models.CharField(
        "rating",
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )

    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"