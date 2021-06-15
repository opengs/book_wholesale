from datetime import datetime, date
from typing import List
from pydantic import BaseModel, Field

class BookMixIn(BaseModel):
    author: str = Field(..., max_length=255, description="Book author")
    title: str = Field(..., max_length=255, description="Book title")
    description: str = Field(None, description="Comprehensive description of the book")
    publication_date: date = Field(..., description="Date of the publication")
    info: str = Field(None, description="Additional technical information")
    price: int = Field(..., ge=0, description="Price per unite")
    count_in_stock: int = Field(0, ge=0, description="Books awailable currently in the stock")
    discount: int = Field(None, ge=0, description="Discount in price units")

    class Config():
        orm_mode = True

class BookInDB(BookMixIn):
    id: int = Field(..., ge=0, description="Identification number of the book")
    
    class Config():
        orm_mode = True

class BooksGetAllRequest(BaseModel): pass
class BooksGetAllResponse(BaseModel): 
    books: List[BookInDB] = Field(...)

    class Config():
        orm_mode = True

class BooksCreateRequest(BookMixIn): pass
class BooksCreateResponse(BookInDB): 
    class Config():
        orm_mode = True

class BooksDeleteRequest(BaseModel):
    id: int = Field(..., ge=0, description="Identification number of the book")
class BooksDeleteResponse(BaseModel): pass