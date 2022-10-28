from django.urls import path

from my_musci_app_stan.web.views import home_with_profile, add_album, album_details, edit_album, delete_album, \
    profile_details, profile_delete, profile_create

urlpatterns = [
    path('', home_with_profile, name='home with profile'),
    path('profile/create/', profile_create, name='home with no profile'),


    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/details', profile_details, name='profile details'),
    path('profile/delete', profile_delete, name='profile delete'),

]

