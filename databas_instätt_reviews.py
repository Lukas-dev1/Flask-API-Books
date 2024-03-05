import sqlite3
import random


# Connect to SQLite database
conn = sqlite3.connect('book_review_platform.db')
cursor = conn.cursor()


user = []
reviews = []
pos_review = []


with open('users.txt', 'r') as file:
    
    for line in file:

        user.append(line.strip())

with open('review.txt', 'r', encoding='utf-8') as file:
    
    for line in file:

        reviews.append(line.strip())

with open('positiv_review.txt', 'r', encoding='utf-8') as file:
    
    for line in file:

        pos_review.append(line.strip())



for x in range(int(input("Hur många reviews"))):
    
    rating = random.randint(1, 5)

    if rating >= 3:
        final_review = pos_review[random.randint(0, len(pos_review)-1)]
        print(f"Positiv recension! {final_review}")
    else:
        final_review = reviews[random.randint(0, len(reviews)-1)]
        print(f'Negativ recension! {final_review}')


    cursor.execute('''
        INSERT INTO reviews (book_id, user_name, rating, review_text)
        VALUES (?, ?, ?, ?)
    ''', (random.randint(1, 100), f'{user[random.randint(0, len(user)-1)]}', rating, f'{final_review}'))


conn.commit()
conn.close()
