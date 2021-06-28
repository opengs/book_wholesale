import pytest
from . import get_test_client

from datetime import datetime

@pytest.mark.parametrize("author,title,description,publication_date,info,price,count_in_stock,discount", [
    ("Test author", "Test title", "123132", datetime.now().isoformat(), "info", 100, 12, 10),
    ("Test", "Test title", None, datetime.now().isoformat(), "info", 100, 12, 10),
    ("author", "Test1212 title", "123132", datetime.now().isoformat(), None, 100, 12, 10),
    ("author", "Test1212 title", "123132", datetime.now().isoformat(), None, 100, 0, 0),
])
def test_book(author,title,description,publication_date,info,price,count_in_stock,discount):

    data = {
        "author": author,
        "title": title,
        "publicationDate": publication_date,
        "price": price,
        "description": description,
        "info": info,
        "count_in_stock": count_in_stock,
        "discount": discount
    }
    response = get_test_client().post('/api/books/book', json=data)
    assert response.status_code == 200
    book_id = response.json()["id"]

    response = get_test_client().get('/api/books/book')
    assert response.status_code == 200
    all_books = response.json()["books"]
    assert len(all_books) == 1
    assert all_books[0]["id"] == book_id
    assert all_books[0]["author"] == author
    assert all_books[0]["title"] == title
    assert all_books[0]["publicationDate"] == publication_date.isoformat()
    assert all_books[0]["price"] == price
    assert all_books[0]["description"] == description
    assert all_books[0]["info"] == info
    assert all_books[0]["count_in_stock"] == count_in_stock
    assert all_books[0]["discount"] == discount

    response = get_test_client().delete('/api/books/book', json={ "id": "id" })
    assert response.status_code == 200

