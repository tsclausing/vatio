from django.contrib import admin
from polls.models import Organization, Department, Profile

admin.site.register(Oraganization, Department, Profile)
