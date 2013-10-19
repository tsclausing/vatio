from django.db import models


class Plans(models.Model):
    name = models.CharField(max_length=255)
    fixed_cost = models.DecimalField(default=25.0)
    user_cost = models.DecimalField(default=2.0)
    max_users = models.IntegerField(default=0)
    teams = models.BooleanField(default=False)
