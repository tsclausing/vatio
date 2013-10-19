from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^view/$', 'pto_requests.views.pto_requests', name='pto_requests'),
    url(r'^view/(\d+)/$', 'pto_requests.views.pto_requests', name='pto_requests'),
)
