from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from datetime import date
from .models import Student

def issue_book(request, id):
    book = Book.objects.get(id=id)
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST['student']
        student = Student.objects.get(id=student_id)

        book.is_issued = True
        book.issued_to = student
        book.issue_date = date.today()
        book.save()
        return redirect('book_list')

    return render(request, 'books/issue_book.html', {'book': book, 'students': students})


def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'], 
            author=request.POST['author'],
            isbn=request.POST['isbn'],
            category=request.POST['category'],
            published_date=request.POST['published_date']
        )
        return redirect('book_list')
    return render(request, 'books/add_book.html')

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')

def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.category = request.POST['category']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')

    return render(request, 'books/edit_book.html', {'book': book})


def toggle_issue(request, id):
    book = Book.objects.get(id=id)
    book.is_issued = not book.is_issued
    book.save()
    return redirect('book_list')

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    total_books = Book.objects.count()
    issued_books = Book.objects.filter(is_issued=True).count()
    available_books = Book.objects.filter(is_issued=False).count()

    return render(request, 'books/book_list.html', {
        'books': books,
        'total_books': total_books,
        'issued_books': issued_books,
        'available_books': available_books
    })

from django.contrib.auth import authenticate, login, logout 

def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')

    return render(request, 'books/student_login.html')

from django.contrib.auth.decorators import login_required
from .models import Student, Book

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    books = Book.objects.filter(issued_to=student)

    return render(request, 'books/student_dashboard.html', {
        'student': student,
        'books': books
    })

def student_logout(request):
    logout(request)
    return redirect('student_login')

