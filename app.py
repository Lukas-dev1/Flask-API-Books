from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_path = 'book_review_platform.db'

# Helper function to connect to the database
def connect_db():
    return sqlite3.connect(db_path)


# Endpoint to get books by a specific author
# Endpoint to get all authors
@app.route('/author', methods=['GET'])
def get_authors():
    conn = connect_db()
    cursor = conn.cursor()

    # Execute the query to get all distinct authors
    cursor.execute("SELECT DISTINCT author FROM books")
    authors = cursor.fetchall()

    conn.close()

    if authors:
        # Extract authors from the list of tuples returned by the database
        authors_list = [author[0] for author in authors]
        return jsonify(authors_list)
    else:
        return 'Authors not found', 404



# Endpoint to get all books with optional filtering
@app.route('/books', methods=['GET'])
def get_books():
    conn = connect_db()
    cursor = conn.cursor()

    # Get filtering parameters from the query string
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    # Build the SQL query with optional filters
    query = "SELECT b.*, AVG(r.rating) AS avg_rating FROM books b LEFT JOIN reviews r ON b.book_id = r.book_id WHERE 1"
    params = []
    if title:
        query += " AND b.title LIKE ?"
        params.append(f'%{title}%')
    if author:
        query += " AND b.author LIKE ?"
        params.append(f'%{author}%')
    if genre:
        query += " AND b.genre = ?"
        params.append(genre)

    # Group by book columns to avoid duplicate rows when there are multiple reviews
    query += " GROUP BY b.book_id"

    # Execute the query
    cursor.execute(query, params)
    books = cursor.fetchall()

    conn.close()

    return jsonify(books)

# Endpoint to get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Execute the query to get a specific book by ID
    cursor.execute("SELECT b.*, AVG(r.rating) AS avg_rating FROM books b LEFT JOIN reviews r ON b.book_id = r.book_id WHERE b.book_id=?", (book_id,))
    book = cursor.fetchone()

    conn.close()

    if book:
        return jsonify(book)
    else:
        return 'Book not found', 404

# Endpoint to add one or more books
@app.route('/books', methods=['POST'])
def add_books():
    # Extract data from the request
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    # Iterate through each book in the request and insert into the database
    for book in data['books']:
        cursor.execute('''
            INSERT INTO books (title, author, summary, genre)
            VALUES (?, ?, ?, ?)
        ''', (book['title'], book['author'], book['summary'], book['genre']))


    conn.commit()
    conn.close()

    return 'Books added successfully', 201



# Endpoint to update a single book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Extract data from the request
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    # Update the book information in the database
    cursor.execute('''
        UPDATE books
        SET title=?, author=?, summary=?, genre=?
        WHERE book_id=?
    ''', (data['title'], data['author'], data.get('summary', ''), data.get('genre', ''), book_id))

    conn.commit()
    conn.close()

    return 'Book updated successfully', 200

# Endpoint to delete a single book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Delete the book from the database
    cursor.execute("DELETE FROM books WHERE book_id=?", (book_id,))
    conn.commit()

    conn.close()

    return 'Book deleted successfully', 200

# Endpoint to add a review to a book
@app.route('/reviews', methods=['POST'])
def add_review():
    # Extract data from the request
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    # Insert the review into the database
    cursor.execute('''
        INSERT INTO reviews (book_id, user_name, rating, review_text)
        VALUES (?, ?, ?, ?)
    ''', (data['book_id'], data['user_name'], data['rating'], data['review_text']))

    conn.commit()
    conn.close()

    return 'Review added successfully', 201





# Endpoint to get all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    conn = connect_db()
    cursor = conn.cursor()

    # Execute the query to get all reviews
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()

    conn.close()

    return jsonify(reviews)

# Endpoint to get reviews for a specific book
@app.route('/reviews/<int:book_id>', methods=['GET'])
def get_reviews_by_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Execute the query to get reviews for a specific book
    cursor.execute("SELECT * FROM reviews WHERE book_id=?", (book_id,))
    reviews = cursor.fetchall()

    conn.close()

    return jsonify(reviews)

# Endpoint to get the top 5 books with the highest average ratings
# Endpoint to get the top 5 books with the highest average ratings
@app.route('/books/top', methods=['GET'])
def get_top_books():
    conn = connect_db()
    cursor = conn.cursor()

    # Execute the query to get the top 5 books with highest average ratings
    cursor.execute(
        "SELECT b.*, AVG(r.rating) AS avg_rating "
        "FROM books b "
        "LEFT JOIN reviews r ON b.book_id = r.book_id "
        "GROUP BY b.book_id "
        "ORDER BY avg_rating DESC "
        "LIMIT 5"
    )
    top_books = cursor.fetchall()

    conn.close()

    return jsonify(top_books)




if __name__ == '__main__':
    app.run(debug=True)
