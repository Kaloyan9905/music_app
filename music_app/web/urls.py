from django.urls import path, include

from music_app.web.views import home_page, add_album, details_profile, details_album, edit_album, delete_album, \
    delete_profile, add_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
