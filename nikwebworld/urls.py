from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from nikwebworld.settings import MEDIA_ROOT, STATIC_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #Examples:
    url(r'^$', direct_to_template, {'template':'homepage.html'}, name='home'),
    url(r'^$', direct_to_template, {'template':'About.html'}, name='about_us'),
    url(r'^$', direct_to_template, {'template':'Contact.html'}, name='contact_us'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    # Will serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
