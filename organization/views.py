from vatio.decorators import render_json, render_to
from .models import Organization


def build_organization(id):
    if id:
        organizations = Organization.objects.filter(pk=id)
    else:
        organizations = Organization.objects.all()
    return {
        'orgs': [{
            'id': x.id,
            'name': x.name,
        } for x in organizations]
    }


@render_json()
def organizations_json(request, id=None):
    return build_organization(id)


@render_to('')
def organizations_view(request, id=None):
    return build_organization(id)
