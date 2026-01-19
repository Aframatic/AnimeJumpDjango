from django import forms
from django.forms import ModelForm
from .models import Anime
from django.contrib.auth.models import User


class AddAnime(forms.Form):
    title = forms.CharField(label='Название',
                            required=True,
                            max_length=50,
                            error_messages={
                                'required': 'Поле обязательно',
                                'max_length': 'Максимум 50 символов',
                            })
    description = forms.CharField(label='Описание',
                                  required=True,
                                  max_length=600,
                                  error_messages={
                                      'required': 'Поле обязательно',
                                      'max_length': 'Максимум 600 символов',
                                  })
    episode = forms.IntegerField(label='Эпизод',
                                 required=True,
                                 error_messages={
                                     'required': 'Поле обязательно',
                                 })
    image = forms.ImageField(label='Картинка',
                             required=True,
                             error_messages={
                                 'required': 'Поле обязательно',
                             })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addAnime',
            'placeholder': 'Название аниме',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addDescription',
            'placeholder': 'Описание',
        })
        self.fields['episode'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addEpisode',
            'placeholder': 'Эпизод',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addImage',
            'placeholder': 'Изображение',
        })


class TagForm(forms.Form):
    tag = forms.CharField(label='Tag', max_length=100)


class AnimeNotPublished(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'description', 'episode', 'image', 'published']


class UsersPublish(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
