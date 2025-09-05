from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mensagem']

    def __init__(self):
        super(PostForm, self).__init__()
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control'})

        


    