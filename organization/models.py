from django.db import models

import simple_audit


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=255)
    org = models.OneToOneField(Organization, blank=False)
    dept = models.ManyToManyField(Organization, null=True, related_name='parent+')


simple_audit.register(Organization, Department, Profile)
