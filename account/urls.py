from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^users/$', 'account.views.users_view', name='users_view'),
    url(r'^user/(\d+)/$', 'account.views.users_view', name='users_view'),
)
