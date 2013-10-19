from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vatio.views.index', name='index'),
	url(r'^kitchensink/$', 'vatio.views.kitchensink', name='kitchensink'),
	url(r'^queue/$', 'vatio.views.queue', name='queue'),
	url(r'^teams/$', 'vatio.views.teams', name='teams'),
	url(r'^settings/$', 'vatio.views.settings', name='settings'),
    # url(r'^vatio/', include('vatio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
