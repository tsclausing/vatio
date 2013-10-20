from vatio.decorators import render_json, render_to
from .models import PtoRequest


def build_pto_request(pk):
    pto_requests = PtoRequest.objects.filter(pk=pk) if pk else PtoRequest.objects.all()
    return {
        'pto_requests': [{
            'id': x.id,
            'name': x.user.name,
            'start_datetime': x.start_datetime,
            'end_datetime': x.start_datetime,
            'request_type': x.request_type,
        } for x in pto_requests]
    }


@render_json()
def pto_requests_json(request, id=None):
    return build_pto_request(id)


@render_to('')
def pto_requests_view(request, id=None):
    return build_pto_request(id)
