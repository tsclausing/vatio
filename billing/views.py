from vatio.decorators import render_json
from .models import Plan


@render_json()
def plans(request, id=None):
    if request.method == 'GET':
        if id:
            plans = Plan.objects.filter(pk=id)
        else:
            plans = Plan.objects.all()
        return {
            'plans': [{
                'id': x.id,
                'max_users': x.max_users,
                'name': x.name,
                'teams': x.teams,
                'user_cost': float(x.user_cost),
                'fixed_cost': float(x.fixed_cost),
            } for x in plans]
        }
