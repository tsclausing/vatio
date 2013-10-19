from vatio.decorators import render_to


@render_to('vatio/index.html')
def index(request):
    return {}
