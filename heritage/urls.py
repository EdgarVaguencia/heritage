from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^liberate/', 'core.views.liberateView'),
    url(r'^entity/', 'core.views.entidadView'),
    url(r'^request/$', 'core.views.requestView'),
    url(r'^request/(?P<type_request>\d+)/$', 'core.views.requestView'),
    # Examples:
    # url(r'^$', 'heritage.views.home', name='home'),
    # url(r'^heritage/', include('heritage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
