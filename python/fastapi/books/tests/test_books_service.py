from app.services.books_service import BookService
from app.schemas.book_schema import Book, Chapter, Page
from app.exceptions.book_exception import BookNotFound


def create_book(bookid="100", booktitle="My favorite book", bookauthor="Emmerson"):
    p = Page(id="1", lines=["line 1"])
    c = Chapter(id="Chapter One", title="The starting", pages=[p])
    b = Book(
        id=bookid,
        title=booktitle,
        author=bookauthor,
        publicationYear=2023,
        chapters=[c],
    )
    return b


def test_list_books_empty():
    service = BookService([])
    assert service.list_books() == []


def test_delete_book():
    service = BookService([create_book()])
    assert service.delete_book("100") is None
    try:
        service.get_book("100")
        assert False
    except BookNotFound:
        assert True


def test_delete_book_not_found():
    service = BookService([create_book()])
    assert service.delete_book("100") is None
    try:
        assert service.delete_book("100") is None
        assert False
    except BookNotFound:
        assert True


def test_create_book_with_defaults():
    b = create_book()
    service = BookService([])
    assert service.create_book(b) == b
    b2 = service.get_book("100")
    assert b2.id == "100"
    assert b2.title == "My favorite book"
    assert b2.author == "Emmerson"


def test_get_book():
    b = create_book(bookid="111", booktitle="How to get a book")
    service = BookService([b])
    assert service.get_book("111").title == "How to get a book"
