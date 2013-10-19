from vatio.decorators import render_to


@render_to('vatio/home.html')
def index(request):
    return {}

@render_to('vatio/kitchensink.html')
def kitchensink(request):
	return {}

@render_to('vatio/queue.html')
def queue(request):
	return {}

@render_to('vatio/teams.html')
def teams(request):
	return {}

@render_to('vatio/settings.html')
def settings(request):
	return {}