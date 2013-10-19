from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^all/$', 'organization.views.organizations', name='organizations'),
    url(r'^(\d+)/$', 'organization.views.organizations', name='organizations'),
)
