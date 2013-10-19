from vatio.decorators import render_json
from .models import PtoRequest


@render_json()
def pto_requests(request, id=None):
    if request.method == 'GET':
        if id:
            pto_requests = PtoRequest.objects.filter(pk=id)
        else:
            pto_requests = PtoRequest.objects.all()
        return {
            'pto_requests': {
                'id': x.id,
                'name': x.user.name,
                'start_datetime': x.start_datetime,
                'end_datetime': x.start_datetime,
                'request_type': x.request_type,
            } for x in pto_requests
        }
