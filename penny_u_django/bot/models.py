from django.db import models

# Create your models here.
class User(models.Model):
    slack_id = models.CharField(max_length=30)
    home_city = models.CharField(max_length=150)
    can_teach = models.CharField(max_length=500)
    will_learn = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'