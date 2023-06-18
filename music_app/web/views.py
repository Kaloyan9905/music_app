from django.shortcuts import render, redirect

from music_app.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from music_app.web.models import Profile, Album


def home_page(request):
    profile = Profile.objects.all()

    if not profile:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)

        if form.is_valid():
            form.save()

            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)

        if form.is_valid():
            album.delete()

            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'delete-album.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home page')

    context = {
        'form': form,
        'hide_attrs': True,
    }

    return render(request, 'home-no-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()

            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
