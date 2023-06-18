from django import forms
from django.forms import HiddenInput

from music_app.web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Album Name'
            }),
            'artist': forms.TextInput(attrs={
                'placeholder': 'Artist'
            }),
            'genre': forms.Select(attrs={
                'placeholder': 'Genre'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Image URL'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            }),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = HiddenInput()
        self.fields['email'].widget = HiddenInput()
        self.fields['age'].widget = HiddenInput()


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['album_name'].widget.attrs['disabled'] = True
        self.fields['artist'].widget.attrs['disabled'] = True
        self.fields['genre'].widget.attrs['disabled'] = True
        self.fields['description'].widget.attrs['disabled'] = True
        self.fields['image_url'].widget.attrs['disabled'] = True
        self.fields['price'].widget.attrs['disabled'] = True
