import sys
sys.path.append('..')

import json
from service.scrape import Scrape

# scrape api
search_term = ''
scrape_result = Scrape.scrape_samtrygg_api(search_term)
# format scrape result
listings = scrape_result['SearchResult']
id_to_listing = {}
for listing in listings:
    id_to_listing[listing['ID']] = listing
# store to json file
filepath = '/samtrygg_scrape_results.json'
with open(filepath, "w") as f:
    json_string = json.dumps(id_to_listing, indent=2, sort_keys=True)
    f.write(json_string)