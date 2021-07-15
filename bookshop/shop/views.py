from django.shortcuts import render, get_object_or_404
from .models import Genre, Book
from cart.forms import CartAddBookForm


def book_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    return render(request,
                  'shop/book/list.html',
                  {'genre': genre,
                   'genres': genres,
                   'books': books})


def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book/detail.html', {'book': book,
                                                        'cart_book_form': cart_book_form})