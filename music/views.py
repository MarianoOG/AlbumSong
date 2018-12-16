# -*- coding: utf-8 -*-
from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .models import Album, Song


class AlbumList(generic.ListView):
    model = Album
    template_name = 'music/album.html'
    context_object_name = 'all_albums'  # Defualt name is object_list


class AlbumDetail(generic.DetailView):
    model = Album
    template_name = 'music/detail_album.html'


class AlbumCreate(CreateView):
    model = Album
    template_name = 'music/create_album.html'
    fields = ['artist', 'title', 'genre', 'cover']


class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'music/create_album.html'
    fields = ['artist', 'title', 'genre', 'cover']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:list_album')


class SongList(generic.ListView):
    model = Song
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'  # Defualt name is object_list


class SongDetail(generic.DetailView):
    model = Song
    template_name = 'music/detail_song.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        song = get_object_or_404(Song, slug=slug)
        album = get_object_or_404(Album, pk=song.album.id)
        context = {'song': song, 'album': album}
        return context


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'youtube_video_ID']


def create_song(request, slug):
    form = SongForm(request.POST or None)
    album = get_object_or_404(Album, slug=slug)

    if form.is_valid():
        album_songs = album.song_set.all()
        for song in album_songs:
            if song.title == form.cleaned_data.get("title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.save()
        return redirect(reverse_lazy('music:detail_song',
                                     kwargs={'slug': song.slug}))
    else:
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'music/create_song.html', context)


def update_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    album = get_object_or_404(Album, pk=song.album.id)

    form = SongForm(request.POST or None, instance=song)

    if form.is_valid():
        song = form.save(commit=False)
        song.save()
        return redirect(reverse_lazy('music:detail_song',
                                     kwargs={'slug': song.slug}))
    else:
        form = SongForm(instance=song)
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'music/create_song.html', context)


class SongDelete(DeleteView):
    model = Song

    def get_success_url(self):
        slug = self.kwargs['slug']
        song = get_object_or_404(Song, slug=slug)
        return reverse_lazy('music:detail_album', kwargs={'slug': song.album.slug})


def favorite_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    if song.is_favorite:
        song.is_favorite = False
    else:
        song.is_favorite = True
    song.save()
    
    form = request.POST
    print(form.get('page'))
    if form.get('page') == 'detail_song':
        return redirect(reverse_lazy('music:detail_song', kwargs={'slug': song.slug}))
    elif form.get('page') == 'detail_album':
        return redirect(reverse_lazy('music:detail_album', kwargs={'slug': song.album.slug}))
            
    return redirect('music:list_song')
