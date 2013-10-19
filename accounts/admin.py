from django.contrib import admin
from accounts.models import Organization, Department, Profile

admin.site.register(Oraganization, Department, Profile)
