from django.contrib.auth.models import User
from django.shortcuts import redirect

from vatio.decorators import render_json, render_to
from Organizations.models import Organization, Department

from .forms import ManagerUserInviteForm
from .models import PendingUserInvite
from .emails import user_invite_notification


def build_users(id):
    if id:
        users = User.objects.filter(pk=id)
    else:
        users = User.objects.filter(is_superuser=False)
    return {
        'users': [{
            'id': x.id,
            'email': x.email,
            'first_name': x.first_name,
            'last_name': x.last_name, 'phone': x.profile.phone,
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
        } for x in users]
    }


@render_json()
def users_json(request, id=None):
    return build_users(id)


@render_to('')
def users_view(request, id=None):
    return build_users(id)


@render_to('account/invite_users.html')
def manager_invite_users(request):
    org = Organization.objects.get(pk=request.user.org.id)
    dept = Department.objects.filter(pk_in=request.user.dept.all().values_list('id'))
    if request.method == 'POST':
        form = ManagerUserInviteForm(request.POST)
        users_list = []
        if form.is_valid():
            for email in form.cleaned_data['email_list']:
                pui = PendingUserInvite(
                    email=email,
                    org=org,
                    dept=dept,
                    is_active=True
                )
                pui.save()
                user_invite_notification(pui.uuid)
                users_list.append(email)
        return redirect('account_view')
    else:
        form = ManagerUserInviteForm()
    return {
        'form': form,
        'org_name': org.name,
        'org_id': org.id
    }
