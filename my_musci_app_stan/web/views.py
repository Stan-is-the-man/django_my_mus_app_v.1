from django.shortcuts import render, redirect

from my_musci_app_stan.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from my_musci_app_stan.web.models import Profile, Album


# extra def:
def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None
    # except Profile.DoesNotExist as ex:
    #     return None


# extra def
def profile_create(request):
    if get_profile() is not None:
        return redirect('index')
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile_exists': True,
    }

    return render(request, 'home-no-profile.html', context)


def home_with_profile(request):
    profile = get_profile()

    if profile is None:
        return redirect('home with no profile')
        # same as return profile_create(request)

    albums = Album.objects.all()
    context = {
        'albums': albums,

    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,

    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = EditAlbumForm(instance=album)
    context = {

        'form': form,
        'album': album,

    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {

        'form': form,
        'album': album,

    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    total_albums = len(albums)
    context = {
        'profile': profile,
        'total_albums': total_albums,

    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile_for_delete = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile_for_delete)
        if form.is_valid():
            form.save()
            return redirect('home with no profile')
    else:
        form = DeleteProfileForm(instance=profile_for_delete)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
