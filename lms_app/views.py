from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = CatForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

        
    context={
        'category':Category.objects.all(),
        'books':Books.objects.all(),
        'form':BookForm(),
        'numbooks':Books.objects.filter(active=True).count(),
        'booksolid':Books.objects.filter(status='sold').count(),
        'bookavaileble':Books.objects.filter(status='available').count(),
        'bookrental':Books.objects.filter(status='rented').count(),
        'formcat':CatForm(),
    }
    return render(request,'pages/index.html',context)
def books(request):
    search = Books.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search= search.filter(title__icontains=title)

    context={
        'category':Category.objects.all(),
        'books':search,
        'formcat':CatForm(),
    }
    return render(request,'pages/books.html',context)

def update(request, id):
    book_id = Books.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context={
        'form':book_save,
    }
    return render(request,'pages/update.html',context)


def delete(request,id):
    book_delete=get_object_or_404(Books,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
