from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^google3d8b31bd23ec2d59.html$', views.google, name="googleverify"),
    url(r'^robots.txt$', views.robots, name="robots"),
    url(r'^sitemap.xml$', views.sitemap, name="sitemap"),
]
