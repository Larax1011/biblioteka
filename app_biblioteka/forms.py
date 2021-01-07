from django.forms import ModelForm, Form
import django.forms as f
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

