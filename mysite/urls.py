from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^MyDjango/', include('MyDjango.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
