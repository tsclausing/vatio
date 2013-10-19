from django.contrib.auth.models import User

from vatio.decorators import render_json


@render_json()
def users_view(request, id=None):
    if request.method == 'GET':
        if id:
            users = User.objects.filter(pk=id)
        else:
            users = User.objects.filter(is_superuser=False)
        return {
            'pto_requests': {
                'id': x.id,
                'email': x.email,
                'first_name': x.first_name,
                'last_name': x.last_name,
                'phone': x.profile.phone,
                'org': {
                    'id': x.profile.org.id,
                    'name': x.profile.org.name,
                },
                'dept': [{
                    'id': z.id,
                    'name': z.name,
                } for z in x.profile.dept.all()],
                'is_org_admin': x.profile.is_org_admin,
                'is_org_delegate': x.profile.is_org_delegate,
                'is_dept_admin': x.profile.is_dept_admin,
                'timezone': x.profile.timezone,
            } for x in users
        }
