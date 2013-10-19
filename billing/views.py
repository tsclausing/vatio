from vatio.decorators import render_to
from .models import Plan


@render_to('vatio/index.html')
def plans_selection(request):
    plans = Plan.objects.all()
    return {
        'plans': plans
    }
