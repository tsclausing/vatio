from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^all/json/$', 'pto_requests.views.pto_requests_json', name='pto_requests_json'),
    url(r'^(\d+)/json/$', 'pto_requests.views.pto_requests_json', name='pto_requests_json'),
    url(r'^all/$', 'pto_requests.views.pto_requests_view', name='pto_requests_view'),
    url(r'^(\d+)/$', 'pto_requests.views.pto_requests_view', name='pto_requests_view'),
)
