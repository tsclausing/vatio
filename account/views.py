from django.contrib.auth.models import User

from vatio.decorators import render_json
from .models import Profile,


@render_json()
def users_view(request, id=None):
    if request.method == 'GET':
        if id:
            pto_requests = PtoRequest.objects.filter(pk=id)
        else:
            pto_requests = PtoRequest.objects.filter(pk=request.user.id)
        return {
            'pto_requests': {
                'id': x.id,
                'name': x.user.name,
                'start_datetime': x.start_datetime,
                'end_datetime': x.start_datetime,
                'request_type': x.request_type,
            } for x in pto_requests
        }
