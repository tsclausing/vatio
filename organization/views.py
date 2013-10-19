from vatio.decorators import render_json
from .models import Organization


@render_json()
def organizations(request, id=None):
    if request.method == 'GET':
        if id:
            organizations = Organization.objects.filter(pk=id)
        else:
            organizations = Organization.objects.all()
        return {
            'plans': {
                'id': x.id,
                'name': x.name,
            } for x in organizations
        }
