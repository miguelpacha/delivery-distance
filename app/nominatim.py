from requests import get

NOMINATIM_URL = "https://nominatim.openstreetmap.org"
SEARCH_URL = NOMINATIM_URL+"/search"

def search_nominatim(query):
    return get(
        SEARCH_URL,
        params = { 'q': query, 'format': 'json', 'address_details': 1 }
    ).json()
