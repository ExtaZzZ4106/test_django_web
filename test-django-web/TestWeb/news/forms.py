from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post name'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post anons'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Post text'
            }),
        }