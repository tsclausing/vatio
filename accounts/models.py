from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

import simple_audit


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=255)
    org = models.OneToOneField(Organization, blank=False)
    dept = models.ManyToManyField(Organization, null=True, related_name='parent+')


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    org = models.OneToOneField(Organization, null=True)
    dept = models.ManyToManyField(Organization, null=True, related_name='profile+')
    is_org_admin = models.BooleanField(default=False)
    timezone = models.CharField(max_length=255, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    """ Don't create when testing or using loaddata.
    See http://stackoverflow.com/questions/3499791/how-do-i-prevent-fixtures-from-conflicting-with-django-post-save-signal-code """
    if created and not kwargs.get('raw', False):
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User, dispatch_uid='0a0bd29e01d9418fb9e20635a7761800')

simple_audit.register(Organization, Department, Profile)
