import requests
import config

def search_companies(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": query,
        "key": config.GOOGLE_MAPS_KEY
    }

    r = requests.get(url, params=params)
    data = r.json()

    companies = []

    for place in data.get("results", []):
        companies.append({
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "rating": place.get("rating")
        })

    return companies