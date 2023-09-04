"""
Main module, starts the http service.
"""
import logging
import os
import uvicorn
from fastapi import FastAPI
from app.schemas.book_schema import Book, List
from app.services.books_service import BookService


FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "INFO"))


server = FastAPI()
service = BookService([])


@server.get("/books", response_model=List[Book])
async def list_books():
    logging.info("Getting list of books.")
    return service.list_books()


@server.post("/books", response_model=Book, status_code=201)
async def create_book(book: Book):
    logging.info(f"Creating book id {book.id}")
    return service.create_book(book)


@server.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: str):
    logging.info(f"Getting book id {book_id}")
    return service.get_book(book_id)


@server.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: Book):
    logging.info(f"Updating book id {book_id}")
    return service.update_book(book_id, book)


@server.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: str):
    logging.info(f"Deleting book id {book_id}")
    return service.delete_book(book_id)


if __name__ == "__main__":
    uvicorn.run("app.main:server", host="0.0.0.0", port=8000, reload=True)
