from django.db import models

#import simple_audit


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    org = models.ManyToManyField(Organization, null=True, blank=True, related_name='departments+')

    def __str__(self):
        return self.name

#simple_audit.register(Organization, Department)
