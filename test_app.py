import pytest
from app import app

# Fixture för att skapa en klient för testning
@pytest.fixture
def klient():
    return app.test_client()

# test för att lägga till böcker
def test_bocker_rutt(klient):
    svar = klient.post('/books', json={'books': []})
    assert svar.status_code == 201

# test för att hämta toppböcker
def test_hamta_top_bocker_rutt(klient):
    svar = klient.get('/books/top')
    assert svar.status_code == 200

# test för att hämta recensioner
def test_hamta_recensioner_rutt(klient):
    svar = klient.get('/reviews')
    assert svar.status_code == 200

# test för att hämta recensioner för en specifik bok
def test_hamta_recensioner_for_bok_rutt(klient):
    bok_id_for_test = 1
    svar = klient.get(f'/reviews/{bok_id_for_test}')
    assert svar.status_code == 200

# test för att lägga till en recension
def test_lagg_till_recension_rutt(klient):
    
    recensionsdata_for_test = {
        'book_id': 1,
        'user_name': 'John Doe',
        'rating': 4,
        'review_text': 'Fantastisk bok!',
    }
    svar = klient.post('/reviews', json=recensionsdata_for_test)
    assert svar.status_code == 201

# test för att radera en bok
def test_radera_bok_rutt(klient):
    bok_id_for_test = 2
    svar = klient.delete(f'/books/{bok_id_for_test}')
    assert svar.status_code == 200

# test för att uppdatera en bok
def test_uppdatera_bok_rutt(klient):
    bok_id_for_test = 1
    uppdaterad_bokdata = {
        'title': 'Uppdaterad Titel',
        'author': 'Uppdaterad Författare',
        'summary': 'Uppdaterad Sammanfattning',
        'genre': 'Uppdaterad Genre',
    }
    svar = klient.put(f'/books/{bok_id_for_test}', json=uppdaterad_bokdata)
    assert svar.status_code == 200

# test för att hämta en bok med ett specifikt ID
def test_hamta_bok_med_id_rutt(klient):
    bok_id_for_test = 1
    svar = klient.get(f'/books/{bok_id_for_test}')
    assert svar.status_code == 200 or svar.status_code == 404

# test för att lägga till flera böcker
def test_lagg_till_bocker_rutt(klient):
    bokdata_for_test = {
        'books': [
            {'title': 'Bok1', 'author': 'Författare1', 'summary': 'Sammanfattning1', 'genre': 'Genre1'},
            {'title': 'Bok2', 'author': 'Författare2', 'summary': 'Sammanfattning2', 'genre': 'Genre2'},
            # Lägg till fler böcker om det behövs
        ]
    }
    svar = klient.post('/books', json=bokdata_for_test)
    assert svar.status_code == 201

# test för att hämta böcker med filterparametrar
def test_hamta_bocker_rutt(klient):
    fraga_parametrar_for_test = {
        'title': 'Test Ti',
        'author': 'Test Författare',
        'genre': 'Test Genre',
    }
    svar = klient.get('/books', query_string=fraga_parametrar_for_test)
    assert svar.status_code == 200



# KOMMENTAR Jag resonerar att testa att det funkar in princip. Jag kör inte några svåra tester för jag vill hålla det så simpelt som möjligt
if __name__ == '__main__':
    # Kör testerna med pytest
    pytest.main()
