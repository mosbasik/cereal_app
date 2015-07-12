from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cereal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^manufacturers/$', 'main.views.manufacturers'),
    url(r'^manufacturers/(?P<mfr_id>\w+)/$', 'main.views.mfr_details'),
)
