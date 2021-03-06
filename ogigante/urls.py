from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'core.views.erro404'

urlpatterns = patterns(
    '',
    url(r'^static/(.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    url(r'^contribua$', 'core.views.new_entry', name='new_entry'),
    url(r'^entry/(\d+)/$', 'core.views.entry', name='entry'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.index', dict(kind='all'), name='index'),
    url(r'^(?P<kind>\w+)/$', 'core.views.index', name='filtered_index'),
)
