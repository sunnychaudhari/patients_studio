from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_stats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'p_app.views.homepage', name='home'),
    url(r'^patient_details/(?P<p_id>[\w-]+)$', 'p_app.views.homepage', name='details'),
    url(r'^admin/', include(admin.site.urls)),
)
