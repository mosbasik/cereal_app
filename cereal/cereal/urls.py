from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cereal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'main.views.home'),
    url(r'^manufacturers/$', 'main.views.manufacturers'),
    url(r'^manufacturers/(?P<mfr_id>\w+)/$', 'main.views.mfr_details'),
    url(r'^cereals/$', 'main.views.cereals'),
    url(r'^cereals/(?P<cereal_id>\w+)/$', 'main.views.cereal_details'),
)
