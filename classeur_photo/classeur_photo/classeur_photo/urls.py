from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import HttpResponseRedirect


urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('album/welcome/')),
    url(r'^album/', include('album.urls')),
    url(r'^admin/', admin.site.urls),
]

