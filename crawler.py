# crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def crawl_site(base_url, max_pages=30):
    visited = set()
    to_visit = [base_url]
    all_pages = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "lxml")
            content_tags = soup.find_all(['h1', 'h2', 'h3', 'p', 'li'])
            page_text = " ".join(tag.get_text(strip=True) for tag in content_tags)
            all_pages.append((url, page_text, soup))

            # find internal links
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    if full_url not in visited:
                        to_visit.append(full_url)

            visited.add(url)
            time.sleep(0.5)  # wait a bit to be polite

        except Exception as e:
            print(f"Failed to crawl {url}: {e}")
            continue

    return all_pages