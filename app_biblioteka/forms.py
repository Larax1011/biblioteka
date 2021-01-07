from django.forms import ModelForm, Form
import django.forms as f
from .models import Article


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'content']

