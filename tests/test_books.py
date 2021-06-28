from . import get_test_client

from datetime import datetime

def test_book():
    author = "Test author"
    title = "Test title"
    publication_date = datetime.now().isoformat()
    price = 100

    data = {
        "author": author,
        "title": title,
        "publicationDate": publication_date,
        "price": price
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
    assert all_books[0]["publicationDate"] == publication_date
    assert all_books[0]["price"] == price

    response = get_test_client().delete('/api/books/book', json={ "id": "id" })
    assert response.status_code == 200

