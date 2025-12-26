import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

class DocumentationCrawler:

    def __init__(self, max_pages=20):
        self.max_pages = max_pages

    def fetch(self, url):
        try:
            print("Fetching:", url)
            resp = requests.get(url, headers=HEADERS, timeout=10, stream=True)

            # Read only first 2 MB to avoid huge HTML dumps
            content = resp.raw.read(2_000_000, decode_content=True)

            if resp.status_code != 200:
                print("Skipped (status):", resp.status_code)
                return None

            return BeautifulSoup(content, "html.parser")

        except Exception as e:
            print("Fetch error:", e)
            return None

    def parse_sections(self, soup):
        sections = []
        for h in soup.find_all(["h1", "h2", "h3"]):
            title = h.get_text(strip=True)
            text_parts = []
            node = h.find_next_sibling()

            while node and node.name not in ["h1", "h2", "h3"]:
                text_parts.append(node.get_text(" ", strip=True))
                node = node.find_next_sibling()

            sections.append({
                "title": title,
                "text": " ".join(text_parts),
                "subsections": {},
            })

        soup["_parsed"] = sections
        return sections

    def crawl(self, urls):
        pages = []
        visited = set()
        queue = list(urls)

        while queue and len(pages) < self.max_pages:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            soup = self.fetch(url)
            if not soup:
                continue

            self.parse_sections(soup)
            pages.append((url, soup))

        print("Total pages collected:", len(pages))
        return pages
