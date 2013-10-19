import json
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import render


def render_json(mimetype='application/json'):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, dict):
                return HttpResponse(json.dumps(output), mimetype=mimetype)
            return output
        return wrapper
    return renderer


def render_to(template, mimetype='text/html'):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, dict):
                return render(request, template, output, content_type=mimetype)
            return output
        return wrapper
    return renderer
