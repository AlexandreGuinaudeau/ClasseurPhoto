from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /album/Vietnam/
    url(r'^$', views.index, name='index'),
    # ex: /album/Vietnam/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]