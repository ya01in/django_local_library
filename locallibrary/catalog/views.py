from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.
from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # counts for genres and books that contain a particular word (case insensitive)
    num_genre = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='programming')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

    # change to one because I only have 4 books
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        # one_liner
        # book = get_object_or_404(Book, pk=primary_key)
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    # paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        # one_liner
        author = get_object_or_404(Author, pk=primary_key)

        return render(request, 'catalog/author_detail.html', context={'author': author})