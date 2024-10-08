from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm, AuthorForm


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form})


def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/author_form.html', {'form': form})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all().select_related('author')
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


def search_books(request):
    query = request.GET.get('query')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__name__icontains=query)
    return render(request, 'books/search_result.html', {'books': books})


def filter_books(request):
    return render(request, 'books/filter_books.html')


def filtered_results(request):
    price = request.GET.get('price')
    max_price = request.GET.get('max_price')
    date = request.GET.get('date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    books = Book.objects.all()

    if start_date and end_date:
        books = books.filter(published_date__range=[start_date, end_date])
    if price:
        books = books.filter(price=price)
    if max_price:
        books = books.filter(price__lte=max_price)
    if date:
        books = books.filter(published_date=date)

    return render(request, 'books/filtered_results.html', {'books': books})


def delete_filtered_books(request):
    if request.method == 'POST':
        books_to_delete = request.POST.getlist('books_to_delete')

        if books_to_delete:
            Book.objects.filter(id__in=books_to_delete).delete()

    return redirect('filter_books')


def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)

    if request.method == 'POST':
        author.delete()
        return redirect('author_list')  # به صفحه لیست نویسندگان یا هر صفحه دیگری که مناسب است هدایت شود

    return render(request, 'books/confirm_delete_author.html', {'author': author, 'books': books})
