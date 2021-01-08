from django.forms import ModelForm
from .models import Book
from .models import Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'content', 'author']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
