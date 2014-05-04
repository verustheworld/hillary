from django.conf.urls import patterns, include, url
from books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hillary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.tmp, name='index')
)
