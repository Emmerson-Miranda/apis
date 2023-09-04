from pydantic import BaseModel
from typing import List


class Page(BaseModel):
    """
    Page Pydantic model.
    """

    id: str
    lines: List[str]


class Chapter(BaseModel):
    """
    Chapter Pydantic model.
    """

    id: str
    title: str
    pages: List[Page]


class Book(BaseModel):
    """
    Book Pydantic model.
    """

    id: str
    title: str
    author: str
    publicationYear: int
    chapters: List[Chapter]
