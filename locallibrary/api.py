from ninja import NinjaAPI
from catalog.models import Author, Genre, Language
from ninja import Schema
from typing import List, Optional
from datetime import date
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class GenreSchema(Schema):
    id: int
    name: str

@api.post("/genres")
def create_genre(request, payload: GenreSchema):
    genre = Genre.objects.create(**payload.dict())
    return {"id": genre.id}

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}")
def update_genre(request, genre_id: int, payload: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return {"success": True}

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

class LanguageSchema(Schema):
    id: int
    name: str

@api.post("/languages")
def create_language(request, payload: LanguageSchema):
    language = Language.objects.create(**payload.dict())
    return {"id": language.id}

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}")
def update_languages(request, language_id: int, payload: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return {"success": True}

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}

class AuthorSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: date
    date_of_death: Optional[date]

@api.post("/authors")
def create_author(request, payload: AuthorSchema):
    author = Author.objects.create(**payload.dict())
    return {"id": author.id}

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.put("/authors/{author_id}")
def update_authors(request, author_id: int, payload: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return {"success": True}

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}
