from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^plans/$', 'billing.views.plans', name='plans'),
    url(r'^plans/(\d+)/$', 'billing.views.plans', name='plans'),

)