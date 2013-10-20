from vatio.decorators import render_json, render_to
from .models import Plan


def build_plan(pk):
    plans = Plan.objects.filter(pk=pk) if pk else Plan.objects.all()
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


@render_json()
def plans_json(request, id=None):
    return build_plan(id)

@render_to('')
def plans_view(request, id=None):
    return build_plan(id)
