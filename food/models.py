from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(verbose_name="Food Name", max_length=200)
    calories = models.FloatField(verbose_name="Calories (kcal)")
    total_fat = models.FloatField(verbose_name="Total Fat (g)")
    saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)")

    def __str__(self):
        return "%s" % self.name

class Meal(models.Model):
    BREAKFAST = 1
    LUNCH = 2
    MEAL_TIME_TYPES = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch") 
     )	
    food = models.ForeignKey(Food, verbose_name="Food",on_delete = models.CASCADE)
    serving_size = models.IntegerField(verbose_name="Serving Size")
    meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPES)

    def get_total_calories(self):
    	return self.serving_size * self.food.calories
