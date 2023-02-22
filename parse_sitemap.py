import requests
from bs4 import BeautifulSoup


# Recursive function to parse sitemap URLs
def parse_sitemap(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    links = soup.find_all('loc')
    for link in links:
        print(link.text)
        if link.text.endswith('.xml'):
            parse_sitemap(link.text)


# URL of the parent sitemap
sitemap_url = 'https://site.com/sitemap_index.xml'

# Parse the parent sitemap and its child sitemaps recursively
parse_sitemap(sitemap_url)
