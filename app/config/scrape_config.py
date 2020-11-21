
SAMTRYGG_JSON_API_URL = 'https://www.samtrygg.se/RentalObject/SearchResult'
SAMTRYGG_DATASTORE_FILEPATH = '/datastore/samtrygg_data.json'
SAMTRYGG_PROCESSED_DATASTORE_FILEPATH = '/datastore/processed_samtrygg_data.json'
SAMTRYGG_PROCESSED_UNSEEN_DATASTORE_FILEPATH = '/datastore/processed_unseen_samtrygg_data.json'

BLOCKET_SEARCH_JSON_API_URL = 'https://api.qasa.se/v1/homes/search'
BLOCKET_LISTING_JSON_API_URL = 'https://api.qasa.se/v1/homes/'
BLOCKET_JSON_API_HEADERS = {
    "Connection": "keep-alive",
    "Accept": "application/json",
    "X-Brand": "X-Brand",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://bostad.blocket.se",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://bostad.blocket.se/",
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8,hr;q=0.7,sv;q=0.6"
}