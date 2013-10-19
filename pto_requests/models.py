from django.db import models
from django.contrib.auth.models import User


class PtoRequest(models.Model):
    user = models.OneToOneField(User, unique=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    request_type = models.CharField(max_length=255, blank=True)
