from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /album/
    url(r'^$', views.index, name='index'),
    # ex: /album/create/
    url(r'^create/$', views.create, name='detail'),
    # ex: /album/vietnam_2016/
    url(r'^(?P<album_permalink>[\w_]+)/$', views.detail, name='detail'),
    # ex: /album/vietnam_2016/import
    url(r'^(?P<album_permalink>[\w_]+)/settings/', views.settings, name='detail'),
    # ex: /album/vietnam_2016/import
    url(r'^(?P<album_permalink>[\w_]+)/import/', views.import_images, name='detail'),
]