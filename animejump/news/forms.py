from django import forms


class AddNews(forms.Form):
    title = forms.CharField(label='Название',
                            required=True,
                            max_length=50,
                            error_messages={
                                'required': 'Поле обязательно',
                                'max_length': 'Максимум 50 символов',
                            })
    description = forms.CharField(label='Описание',
                                  required=True,
                                  max_length=300,
                                  error_messages={
                                      'required': 'Поле обязательно',
                                      'max_length': 'Максимум 300 символов',
                                  })
    image = forms.ImageField(label='Картинка',
                             required=True,
                             error_messages={
                                 'required': 'Поле обязательно',
                             })
    full_text = forms.CharField(label='Описание',
                                  required=True,
                                  max_length=1500,
                                  error_messages={
                                      'required': 'Поле обязательно',
                                      'max_length': 'Максимум 1500 символов',
                                  })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addNews',
            'placeholder': 'Название аниме',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addDescription',
            'placeholder': 'Описание',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addImage',
            'placeholder': 'Изображение',
        })
        self.fields['full_text'].widget.attrs.update({
            'class': 'form-control',
            'id': 'addFullText',
            'placeholder': 'Полная статья',
        })