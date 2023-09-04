from app.exceptions.book_exception import BookNotFound


class BookService:
    """
    Books business logic.
    """

    def __init__(self, books):
        self._books_data = books

    def list_books(self):
        return self._books_data

    def create_book(self, book):
        self._books_data.append(book)
        return book

    def get_book(self, book_id):
        for book in self._books_data:
            if book.id == book_id:
                return book
        raise BookNotFound(book_id)

    def update_book(self, book_id, book):
        for i, existing_book in enumerate(self._books_data):
            if existing_book.id == book_id:
                self._books_data[i] = book
                return book
        raise BookNotFound(book_id)

    def delete_book(self, book_id):
        for i, book in enumerate(self._books_data):
            if book.id == book_id:
                del self._books_data[i]
                return None
        raise BookNotFound(book_id)
