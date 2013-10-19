from vatio.decorators import render_to


@render_to('vatio/home.html')
def index(request):
    return {}
