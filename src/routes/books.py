from fastapi import Depends, Body
from fastapi.routing import APIRouter

from ..database.models.book import Book

from .models.book import BooksGetAllRequest, BooksGetAllResponse, BooksCreateRequest, BooksCreateResponse, BooksDeleteRequest, BooksDeleteResponse

router = APIRouter()

@router.get("/all", response_model=BooksGetAllResponse)
async def get_all(data: BooksGetAllRequest = Depends()):
    '''Get all books'''
    books = await Book.all().values()
    return { "books": books }

@router.post("/book", response_model=BooksCreateResponse)
async def create(data: BooksCreateRequest = Body(...)):
    '''Create new book'''
    book = await Book.create(**data.dict())
    return BooksCreateResponse.from_orm(book)

@router.delete("/book", response_model=BooksDeleteResponse)
async def delete(data: BooksDeleteRequest = Body(...)):
    '''Delete book'''
    book = await Book.get_or_none(id=data.id)
    if book != None:
        await book.delete()
    return BooksDeleteResponse()