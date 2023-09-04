from app import main
from fastapi.testclient import TestClient

client = TestClient(main.server)


def get_dummy_book():
    return {
        "id": "1",
        "title": "1984",
        "author": "George Orwell",
        "publicationYear": 1949,
        "chapters": [
            {
                "id": "c1",
                "title": "Chapter 1",
                "pages": [
                    {
                        "id": "p1",
                        "lines": [
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                        ],
                    }
                ],
            }
        ],
    }


def test_http_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []


def test_http_post_book():
    book = get_dummy_book()
    headers = {"Content-Type": "application/json"}
    response = client.post("/books", headers=headers, json=book)
    assert response.status_code == 201
    assert response.json() == book


def test_http_get_book():
    book = get_dummy_book()
    headers = {"Content-Type": "application/json"}
    response = client.post("/books", headers=headers, json=book)
    assert response.status_code == 201
    assert response.json() == book

    response = client.get(f"/books/{book['id']}")
    assert response.status_code == 200
    assert response.json() == book


def test_http_delete_book():
    book = get_dummy_book()
    test_http_post_book()

    response = client.delete(f"/books/{book['id']}")
    assert response.status_code == 204


def test_http_put_book():
    expected_title = "New book title"
    book = get_dummy_book()
    headers = {"Content-Type": "application/json"}
    response = client.post("/books", headers=headers, json=book)
    assert response.status_code == 201
    assert response.json() == book

    book["title"] = expected_title
    response = client.put(f"/books/{book['id']}", headers=headers, json=book)
    assert response.status_code == 200

    response = client.get(f"/books/{book['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == expected_title
