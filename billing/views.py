from vatio.decorators import render_json
from .models import Plan


@render_json()
def plans(request):
    plans = Plan.objects.all()
    return {
        'plans': [x for x in plans]
    }
