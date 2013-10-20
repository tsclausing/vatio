from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


from organization.models import Organization, Department


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    org = models.ForeignKey(Organization, null=True, blank=True)
    dept = models.ForeignKey(Department, null=True, blank=True)
    is_org_admin = models.BooleanField(default=False)
    is_org_delegate = models.BooleanField(default=False)
    is_dept_admin = models.BooleanField(default=False)
    timezone = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return ' - '.join([
            self.user.username,
            str(self.org),
            str(self.dept),
        ])


def create_user_profile(sender, instance, created, **kwargs):
    """ Don't create when testing or using loaddata.
    See http://stackoverflow.com/questions/3499791/how-do-i-prevent-fixtures-from-conflicting-with-django-post-save-signal-code """
    if created and not kwargs.get('raw', False):
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User, dispatch_uid='0a0bd29e01d9418fb9e20635a7761800')


class PendingUserInvite(models.Model):
    """ Model for storing invited user information
    """
    org = models.OneToOneField(Organization, null=False)
    dept = models.OneToOneField(Department, null=True)
    email = models.EmailField(null=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.email, self.is_active, self.uuid)


