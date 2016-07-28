import os
from configuration import CONFIG

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.template import Context, Template, RequestContext
from django.http import HttpResponse
from django.contrib import messages

from .models import Album, Photo
from .forms import WelcomeForm, NewAlbumForm, ImportImagesForm


def get_template(files):
    if isinstance(files, str):
        files = [files]
    template = ""
    for file_name in files:
        with open(os.path.realpath('album/templates/' + file_name), 'r') as in_f:
            template += in_f.read().replace('\n', '')
    return Template(template)


def welcome(request):
    title = 'Welcome!'
    initial_path = os.path.realpath(os.path.join(__file__, '..', '..', '..', '..', '..', 'Albums'))
    form = WelcomeForm(request.POST, initial={'local_folder': initial_path})
    if form.is_valid():
        local_folder = form.cleaned_data['local_folder']
        if not os.path.isdir(local_folder):
            try:
                os.mkdir(local_folder)
                CONFIG.path = local_folder
                return HttpResponseRedirect('/album/')
            except OSError as e:
                print('ERROR: Could not create local folder %s:\n%s' % (local_folder, str(e)))
                messages.error(request, 'Could not create folder:')
                messages.error(request, local_folder)
        else:
            CONFIG.path = local_folder
            return HttpResponseRedirect('/album/')
    if request.POST.get('local_folder', u'') == u'':
        form = WelcomeForm(initial={'local_folder': initial_path})
    context = RequestContext(request, {
        'title': title,
        'album_list': [],
        'form': form,
        'name': 'welcome',
    })
    t = get_template(['head.html', 'header_navbar.html', 'index.html', 'form.html', 'footer.html']).render(context)
    return HttpResponse(t)


def index(request):
    if not hasattr(CONFIG, 'path'):
        return HttpResponseRedirect('/album/welcome/')
    title = 'Album'
    album_list = Album.objects.order_by('permalink')
    form = NewAlbumForm()
    context = RequestContext(request, {
        'title': title,
        'album_list': album_list,
        'form': form,
        'name': 'index',
    })
    t = get_template(['head.html', 'header_navbar.html', 'index.html', 'form.html', 'footer.html']).render(context)
    return HttpResponse(t)


def detail(request, album_permalink):
    if not hasattr(CONFIG, 'path'):
        return HttpResponseRedirect('/album/welcome/')
    album = get_object_or_404(Album, permalink=album_permalink)
    title = album.name
    form = ImportImagesForm(request.POST)
    context = RequestContext(request, {
        'title': title,
        'album': album,
        'name': 'detail',
        'form': form,
    })
    t = get_template(['head.html', 'header_navbar.html', 'detail.html', 'form.html', 'footer.html']).render(context)
    return HttpResponse(t)


def settings(request, album_permalink):
    if not hasattr(CONFIG, 'path'):
        return HttpResponseRedirect('/album/welcome/')
    album = get_object_or_404(Album, permalink=album_permalink)
    title = album.name + ' - Settings'
    album_list = Album.objects.order_by('permalink')
    context = Context({
        'title': title,
        'album': album,
        'album_list': album_list,
        'name': 'settings',
    })
    t = get_template(['head.html', 'header_navbar.html', 'settings.html', 'footer.html']).render(context)
    return HttpResponse(t)


def create(request):
    if not hasattr(CONFIG, 'path'):
        return HttpResponseRedirect('/album/welcome/')
    form = NewAlbumForm(request.POST)
    if form.is_valid():
        album_name = form.cleaned_data['album_name']
        permalink = form.cleaned_data['permalink']
        a = Album(name=album_name, permalink=permalink)
        a.save()
        try:
            os.mkdir(os.path.join(CONFIG.path, album_name))
        except OSError:
            CONFIG.path = None
        return HttpResponseRedirect('/album/%s' % permalink)
    return HttpResponseRedirect('/album/')

