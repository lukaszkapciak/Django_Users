from django.contrib import admin
from .models import Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['last_name']
    ordering = ['last_name']

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cover']
    search_fields = ['title']
    ordering = ['title']

admin.site.register(Book, BookAdmin)