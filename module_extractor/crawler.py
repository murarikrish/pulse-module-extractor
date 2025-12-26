import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque


class DocumentationCrawler:

    def __init__(self, max_pages=200, timeout=10):
        self.max_pages = max_pages
        self.timeout = timeout
        self.visited = set()

    def is_valid(self, base_domain, link):
        parsed = urlparse(link)
        return (
            parsed.netloc == base_domain
            and link not in self.visited
            and link.startswith("http")
        )

    def crawl(self, start_urls):
        pages = []
        queue = deque(start_urls)
        base_domain = urlparse(start_urls[0]).netloc

        while queue and len(pages) < self.max_pages:
            url = queue.popleft()
            if url in self.visited:
                continue

            self.visited.add(url)

            try:
                resp = requests.get(url, timeout=self.timeout)
                if resp.status_code != 200:
                    continue
            except:
                continue

            soup = BeautifulSoup(resp.text, "lxml")
            pages.append((url, soup))

            for a in soup.find_all("a", href=True):
                link = urljoin(url, a["href"])
                if self.is_valid(base_domain, link):
                    queue.append(link)

        return pages
