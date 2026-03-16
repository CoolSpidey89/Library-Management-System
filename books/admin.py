from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student, Book


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    pass
