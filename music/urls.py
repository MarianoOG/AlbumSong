from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^album$', views.AlbumList.as_view(), name='list_album'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='create_album'),
    url(r'^album/(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='detail_album'),
    url(r'^album/(?P<slug>[-\w]+)/edit$', views.AlbumUpdate.as_view(), name='update_album'),
    url(r'^album/(?P<slug>[-\w]+)/delete$', views.AlbumDelete.as_view(), name='delete_album'),
    
    url(r'^album/(?P<slug>[-\w]+)/addsong$', views.create_song, name='create_song'),

    url(r'^song$', views.SongList.as_view(), name='list_song'),
    url(r'^song/(?P<slug>[-\w]+)$', views.SongDetail.as_view(), name='detail_song'),
    url(r'^song/(?P<slug>[-\w]+)/edit$', views.update_song, name='update_song'),
    url(r'^song/(?P<slug>[-\w]+)/delete$', views.SongDelete.as_view(), name='delete_song'),
    url(r'^song/(?P<slug>[-\w]+)/favorite$', views.favorite_song, name='favorite_song'),
]
