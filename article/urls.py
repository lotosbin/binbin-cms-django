from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from article import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newsdemo.views.home', name='home'),
    # url(r'^newsdemo/', include('newsdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^report/$', views.news_report, name='report'),
	url(r'^article/$', views.news_article, name='article'),
	url(r'^show/(\d+)/$', views.news_aid, name='show'),
)
