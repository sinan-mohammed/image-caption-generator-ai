from utils.logger import logger
import requests
from config.settings import SERPER_API_KEY


def google_search(query):
    logger.info(f"[Search Tool] Searching for: {query}")
    if not SERPER_API_KEY:
        logger.error("[Search Tool] SERPER_API_KEY is missing.")
        return "Search failed: missing SERPER_API_KEY."

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        results = response.json()
        snippets = []

        if "organic" in results:
            for item in results["organic"][:5]:
                snippets.append(item.get("snippet", ""))

        logger.info("[Search Tool] Search completed successfully")
        return "\n".join(snippets)

    except Exception as e:
        logger.error(f"[Search Tool] Error during search: {str(e)}")
        return "Search failed."
