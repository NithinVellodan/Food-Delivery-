import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FoodOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey("web.ViewFood", on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.date.today())
    is_ordered = models.BooleanField(default=False)
    is_deleted= models.BooleanField(default=False)

    


class ViewFood(models.Model):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    TEA = 'tea'
    DINNER = 'dinner'
    FOOD_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (TEA, 'Tea'),
        (DINNER, 'Dinner'),
    ]
    image = models.FileField(upload_to="food/images/")
    title = models.CharField(max_length=255)
    food_type = models.CharField(max_length=20, choices=FOOD_CHOICES)
    price = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
