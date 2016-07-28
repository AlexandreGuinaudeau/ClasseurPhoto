from django import forms


class NewAlbumForm(forms.Form):
    album_name = forms.CharField(label='Album name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'type': 'text'}))
    permalink = forms.SlugField(label='Permalink', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'type': 'text'}))


class WelcomeForm(forms.Form):
    local_folder = forms.CharField(label='Local Folder', max_length=200,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'type': 'text'}))


class ImportImagesForm(forms.Form):
    url_path = forms.URLField(required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}))
    folder_path = forms.FilePathField(path="", allow_folders=True, required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'file'}))
