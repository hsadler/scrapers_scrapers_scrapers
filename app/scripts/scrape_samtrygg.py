import sys
sys.path.append('..')

import json
from service.scrape import Scrape

search_term = ''
scrape_result = Scrape.scrape_samtrygg_api(search_term)
filepath = '/samtrygg_scrape_results.json'
with open(filepath, "w") as f:
    json_string = json.dumps(scrape_result, indent=2, sort_keys=True)
    f.write(json_string)