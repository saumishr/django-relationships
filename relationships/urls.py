from django.conf.urls.defaults import *

urlpatterns = patterns('relationships.views',
    url(r'^$', 'relationship_redirect', name='relationship_list_base'),
    url(r'^(?P<username>[\w.@+-]+)/(?:(?P<status_slug>[\w-]+)/)?$', 'relationship_list', name='relationship_list'),
    url(r'^add/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_handler', {'add': True}, name='relationship_add'),
    url(r'^followers/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', 'get_followers', name='get_followers'),
    url(r'^following/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', 'get_following', name='get_following'),
    url(r'^remove/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_handler', {'add': False}, name='relationship_remove'),
)
