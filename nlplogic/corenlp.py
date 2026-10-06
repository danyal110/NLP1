from textblob import TextBlob
import requests


def search_wikipedia(name):
    url = "https://en.wikipedia.org/w/api.php"

    params = {"action": "query", "format": "json", "list": "search", "srsearch": name}

    headers = {"User-Agent": "NLP1/1.0 (educational project)"}

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    return [item["title"] for item in data["query"]["search"]]


def summarise_wikipedia(name):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + name.replace(" ", "_")

    headers = {"User-Agent": "NLP1/1.0 (educational project)"}

    response = requests.get(
        url,
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    return data["extract"]


def get_text_blob(text):
    return TextBlob(text)


def get_phrases(name):
    text = summarise_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
