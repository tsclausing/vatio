from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^all/json/$', 'organization.views.organizations_json', name='organizations_json'),
    url(r'^(\d+)/json/$', 'organization.views.organizations_json', name='organizations_json'),
    url(r'^all/$', 'organization.views.organizations_view', name='organizations_view'),
    url(r'^(\d+)/$', 'organization.views.organizations_view', name='organizations_view'),
)
