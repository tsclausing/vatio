from django.db import models


class Plans(models.Model):
    name = models.CharField(max_length=255)
    fixed_cost = models.DecimalField(max_digits=8, decimal_places=2, default=25.0)
    user_cost = models.DecimalField(max_digits=8, decimal_places=2, default=2.0)
    max_users = models.IntegerField(default=0)
    teams = models.BooleanField(default=False)
