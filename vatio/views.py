from vatio.decorators import render_to


@render_to('vatio/home.html')
def index(request):
    return {}

@render_to('vatio/kitchensink.html')
def kitchensink(request):
	return {}
