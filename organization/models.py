from django.db import models

import simple_audit


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=255)
    org = models.OneToOneField(Organization, blank=False)
    dept = models.ForeignKey('Department', null=True, blank=True)



simple_audit.register(Organization, Department)
