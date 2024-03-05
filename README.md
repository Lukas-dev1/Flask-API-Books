# Book Review Platform API

## Overview

This is a Flask-based API for a book review platform. The API allows users to perform various operations such as retrieving information about books, authors, reviews, adding books and reviews, updating book details, and more.

## Getting Started

To use this API, ensure you have Python and Flask installed. You can install the required dependencies using the following:

```bash
pip install Flask
```

Clone the repository and navigate to the project directory. Run the following command to start the Flask development server:

```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000/`.

## Endpoints

### 1. Get Authors

- **Endpoint:** `/author`
- **Method:** `GET`
- **Description:** Retrieve a list of all distinct authors.

### 2. Get Books

- **Endpoint:** `/books`
- **Method:** `GET`
- **Description:** Retrieve a list of books with optional filtering by title, author, and genre.

### 3. Get Book by ID

- **Endpoint:** `/books/<int:book_id>`
- **Method:** `GET`
- **Description:** Retrieve information about a specific book using its ID.

### 4. Add Books

- **Endpoint:** `/books`
- **Method:** `POST`
- **Description:** Add one or more books to the platform. Provide book details in the request body.

### 5. Update Book by ID

- **Endpoint:** `/books/<int:book_id>`
- **Method:** `PUT`
- **Description:** Update information about a specific book using its ID. Provide updated details in the request body.

### 6. Delete Book by ID

- **Endpoint:** `/books/<int:book_id>`
- **Method:** `DELETE`
- **Description:** Delete a specific book using its ID.

### 7. Add Review

- **Endpoint:** `/reviews`
- **Method:** `POST`
- **Description:** Add a review for a book. Provide review details in the request body.

### 8. Get All Reviews

- **Endpoint:** `/reviews`
- **Method:** `GET`
- **Description:** Retrieve a list of all reviews.

### 9. Get Reviews by Book

- **Endpoint:** `/reviews/<int:book_id>`
- **Method:** `GET`
- **Description:** Retrieve reviews for a specific book using its ID.

### 10. Get Top 5 Books

- **Endpoint:** `/books/top`
- **Method:** `GET`
- **Description:** Retrieve the top 5 books with the highest average ratings.

## Note

- Ensure you have a SQLite database file named `book_review_platform.db` in the project directory.
- The API is set to run in debug mode (`debug=True`). Change this for a production environment.
- Use appropriate caution and authentication mechanisms before deploying in a production environment.

Feel free to explore and integrate these endpoints into your application!
