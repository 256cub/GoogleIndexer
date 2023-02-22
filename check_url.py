from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from Main import *

# List of URLs to check
urls = ['https://validphp.com/how-to-string-interpolate-output-of-a-method-in-php/', 'https://moneycoma.com/', ]

print(APP_PATH + 'input/client_secrets.json')

# Set up credentials for the Search Console API
creds = Credentials.from_authorized_user_file(APP_PATH + 'input/credentials.json', [
    'https://www.googleapis.com/auth/webmasters.readonly'
]
                                              )
service = build('webmasters', 'v3', credentials=creds)

# Set up credentials for the Search Console API
creds = Credentials.from_authorized_user_file(os.path.expanduser('~/path/to/credentials.json'), ['https://www.googleapis.com/auth/webmasters.readonly'])
service = build('webmasters', 'v3', credentials=creds)

# Check if each URL is indexed by Google using the Search Console API
for url in urls:
    try:
        query = {
            'startDate': '2023-02-19',
            'endDate': '2023-02-19',
            'dimensions': ['page'],
            'dimensionFilterGroups': [{
                'filters': [{
                    'dimension': 'page',
                    'operator': 'equals',
                    'expression': url
                }]
            }]
        }
        response = service.searchanalytics().query(siteUrl=url, body=query).execute()

        if 'rows' in response:
            print(url + ' is indexed by Google')
        else:
            print(url + ' is not indexed by Google')
    except HttpError as error:
        print('An error occurred: %s' % error)
