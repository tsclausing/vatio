from django.db import models

#import simple_audit


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=255)
    org = models.ManyToManyField(Organization, blank=False, null=True)
    dept = models.ForeignKey('Department', null=True, blank=True)


    def __str__(self):
        return ' - '.join([self.name, self.org, self.dept])

#simple_audit.register(Organization, Department)
