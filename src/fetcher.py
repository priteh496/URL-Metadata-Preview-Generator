"""
Fetches and parses URL metadata including Open Graph tags.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict


class URLMetaFetcher:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (compatible; MetaPreviewBot/1.0)"
    }

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def fetch(self, url: str) -> Dict:
        result = {"url": url}
        try:
            resp = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            result["status_code"] = resp.status_code
            result["content_type"] = resp.headers.get("Content-Type", "")
            result["final_url"] = resp.url

            if "text/html" not in result["content_type"]:
                result["error"] = "Not an HTML page"
                return result

            soup = BeautifulSoup(resp.text, "html.parser")

            # Standard meta tags
            result["title"] = soup.title.string.strip() if soup.title else None

            for tag in soup.find_all("meta"):
                name = tag.get("name", "").lower()
                prop = tag.get("property", "").lower()
                content = tag.get("content", "")

                if name in ("description", "author", "keywords"):
                    result[name] = content
                if prop.startswith("og:"):
                    result[prop] = content
                if prop.startswith("twitter:"):
                    result[prop] = content

            # Canonical URL
            canonical = soup.find("link", rel="canonical")
            if canonical:
                result["canonical"] = canonical.get("href")

        except requests.exceptions.Timeout:
            result["error"] = "Request timed out"
        except requests.exceptions.ConnectionError:
            result["error"] = "Could not connect"
        except Exception as e:
            result["error"] = str(e)

        return result
