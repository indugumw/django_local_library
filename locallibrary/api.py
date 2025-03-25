import uuid
from ninja import NinjaAPI
from catalog.models import Author, Genre, Language, Book, BookInstance
from ninja import Schema
from typing import List, Optional
from datetime import date
from django.shortcuts import get_object_or_404
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth)

class GenreSchema(Schema):
    id: int
    name: str

@api.post("/genres", auth=django_auth)
def create_genre(request, payload: GenreSchema):
    genre = Genre.objects.create(**payload.dict())
    return {"id": genre.id}

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}", auth=django_auth)
def update_genre(request, genre_id: int, payload: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return {"success": True}

@api.delete("/genres/{genre_id}", auth=django_auth)
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

class LanguageSchema(Schema):
    id: int
    name: str

@api.post("/languages", auth=django_auth)
def create_language(request, payload: LanguageSchema):
    language = Language.objects.create(**payload.dict())
    return {"id": language.id}

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}", auth=django_auth)
def update_languages(request, language_id: int, payload: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return {"success": True}

@api.delete("/languages/{language_id}", auth=django_auth)
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}

class AuthorSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: date
    date_of_death: Optional[date]

@api.post("/authors", auth=django_auth)
def create_author(request, payload: AuthorSchema):
    author = Author.objects.create(**payload.dict())
    return {"id": author.id}

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.put("/authors/{author_id}", auth=django_auth)
def update_authors(request, author_id: int, payload: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return {"success": True}

@api.delete("/authors/{author_id}", auth=django_auth)
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

class BookSchema(Schema):
    id: int
    title: str
    author_id: int
    summary: str
    isbn: str
    genre: List[int]  

@api.post("/books", auth=django_auth)
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.put("/books/{book_id}", auth=django_auth)
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return {"success": True}

@api.delete("/books/{book_id}", auth=django_auth)
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}

class BookInstanceSchema(Schema):
    id: uuid.UUID
    book_id: int
    imprint: str
    due_back: Optional[date]
    borrower_id: Optional[int]
    status: str

@api.post("/bookinstances", auth=django_auth)
def create_book_instance(request, payload: BookInstanceSchema):
    book_instance = BookInstance.objects.create(**payload.dict())
    return {"id": book_instance.id}

@api.get("/bookinstances/{bookinstance_id}", response=BookInstanceSchema)
def get_book_instance(request, bookinstance_id: uuid.UUID):
    book_instance = get_object_or_404(BookInstance, id=bookinstance_id)
    return book_instance

@api.put("/bookinstances/{bookinstance_id}", auth=django_auth)
def update_book_instance(request, bookinstance_id: uuid.UUID, payload: BookInstanceSchema):
    book_instance = get_object_or_404(BookInstance, id=bookinstance_id)
    for attr, value in payload.dict().items():
        setattr(book_instance, attr, value)
    book_instance.save()
    return {"success": True}

@api.delete("/bookinstances/{bookinstance_id}", auth=django_auth)
def delete_book_instance(request, bookinstance_id: uuid.UUID):
    book_instance = get_object_or_404(BookInstance, id=bookinstance_id)
    book_instance.delete()
    return {"success": True}