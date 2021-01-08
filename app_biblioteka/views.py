from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Review
from .forms import BookForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Library'})
    else:
        return redirect('app_biblioteka:books')


@login_required
def books(req):
    tmp = Book.objects.all()
    return render(req, 'books.html', {'books': tmp})


@login_required
def book(req, id):
    tmp = get_object_or_404(Book, id=id)
    return render(req, 'book.html', {'book': tmp, 'page_title': tmp.title})


@permission_required('app_biblioteka.change_book')
def edit(req, id):
    if req.method == 'POST':
        form = BookForm(req.POST)

        if form.is_valid():
            a = Book.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.content = form.cleaned_data['content']
            a.author = form.cleaned_data['author']
            a.save()
            return redirect('app_biblioteka:books')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Book.objects.get(id=id)
        form = BookForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('app_biblioteka.add_book')
def new(req):
    if req.method == 'POST':
        form = BookForm(req.POST)

        if form.is_valid():
            a = Book(title=form.cleaned_data['title'], content=form.cleaned_data['content'], owner=req.user, author=form.cleaned_data['author'])
            a.save()
            return redirect('app_biblioteka:books')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = BookForm()
        return render(req, 'new.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "books.html")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})