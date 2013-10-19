from django.contrib import admin
from accounts.models import Organization, Department, Profile

admin.site.register(Organization, Department, Profile)
