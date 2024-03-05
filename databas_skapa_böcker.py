import sqlite3
import random


# Connect to SQLite database
conn = sqlite3.connect('book_review_platform.db')
cursor = conn.cursor()



genre = []
sumering = []
forfattare = []
books = []

with open('författare.txt', 'r') as file:
    
    for line in file:
        
        forfattare.append(line.strip())


# Open the file in read mode
with open('böcker.txt', 'r') as file:
    
    for line in file:

        books.append(line.strip())


with open('genre.txt', 'r') as file:
    
    for line in file:
        
        genre.append(line.strip())


# Open the file in read mode
with open('summering.txt', 'r') as file:
    
    for line in file:

        sumering.append(line.strip())
        


#Sätter databasen på plats så den har nått värde med böcker. Du kan köra hur många gånger som helst men det funkar inte. Om du kör flera gånger stannar den.
for i in range(len(books)):
    # Check if the title already exists in the database
    cursor.execute("SELECT COUNT(*) FROM books WHERE title = ?", (f'{books[i]}',))
    count = cursor.fetchone()[0]

    # du får bara köra en gång.
    if count == 0:
        cursor.execute('''
            INSERT INTO books (title, author, summary, genre)
            VALUES (?, ?, ?, ?)
        ''', (f'{books[i]}', f'{forfattare[i]}', f'{sumering[i]}', f'{genre[random.randint(0, 19)]}'))
    else:
        print(f"Boken '{books[i]}' Finns redan skippar detta!")









print("Klart!")
# Commit the changes and close the connection
conn.commit()
conn.close()
