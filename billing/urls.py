from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^all/json/$', 'billing.views.plans_json', name='plans_json'),
    url(r'^(\d+)/json/$', 'billing.views.plans_json', name='plans_json'),
    url(r'^all/$', 'billing.views.plans_view', name='plans_view'),
    url(r'^(\d+)/$', 'billing.views.plans_view', name='plans_view'),
)
