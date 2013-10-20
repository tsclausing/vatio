from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^users/json/$', 'account.views.users_json', name='users_json'),
    url(r'^user/(\d+)/json/$', 'account.views.users_json', name='users_json'),
    url(r'^users/$', 'account.views.users_view', name='users_view'),
    url(r'^user/(\d+)/$', 'account.views.users_view', name='users_view'),
)
