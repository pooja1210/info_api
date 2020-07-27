from django.db import models

# Create your models here.

class User(models.Model):
    user_id =    models.CharField(max_length=30, unique=True)
    real_name =  models.CharField(max_length=254)
    address =    models.CharField(max_length=254)
    def __str__(self):
        return self.real_name
    

class ActivityPeriod(models.Model):
    class Meta:
        verbose_name_plural = "activity_period"
    user_id = models.ForeignKey(User, related_name='activity_period',on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
