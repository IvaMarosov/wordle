import requests

WORDS_URL = "https://cheaderthecoder.github.io/5-Letter-words/words.txt"


def get_list_of_words(url: str = WORDS_URL) -> list[str]:
    """Obtain list of 5-letter words from provided URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()

        if "text" not in response.headers.get("content-type", ""):
            raise ValueError(
                f"Unexpected content type: {response.headers.get('Content-type')}"
            )

        return response.text.splitlines()

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

    except ValueError as e:
        print(f"Data error: {e}")

    return []
