import requests
from bs4 import BeautifulSoup

from Main import *

# URL of the parent sitemap
sitemap_url = SITEMAP_URL


# Recursive function to parse sitemap URLs
def parse_sitemap(url, website_id):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    links = soup.find_all('loc')
    for link in links:
        if link.text.endswith('.xml'):
            parse_sitemap(link.text, website_id)
        else:

            url_id = check_if_row_exist('urls', 'url', hostname_url)
            if not url_id:
                url_columns = dict()
                url_columns['websites_id'] = website_id
                url_columns['url'] = link.text
                url_columns['status'] = DEFAULT_STATUS

                url_id = insert_row_into_table('urls', url_columns)

            print(Fore.WHITE + 'URL', Fore.YELLOW + '{}'.format(url_id), Fore.YELLOW + '{}'.format(link.text))


hostname_url = get_hostname_from_url(sitemap_url)

website_id = check_if_row_exist('websites', 'url', hostname_url)
if not website_id:
    website_columns = dict()
    website_columns['name'] = ''
    website_columns['url'] = hostname_url
    website_columns['status'] = DEFAULT_STATUS

    website_id = insert_row_into_table('websites', website_columns)

print(Fore.WHITE + 'WEBSITE', Fore.YELLOW + '{}'.format(website_id), Fore.YELLOW + '{}'.format(hostname_url))

# Parse the parent sitemap and its child sitemaps recursively
parse_sitemap(sitemap_url, website_id)
