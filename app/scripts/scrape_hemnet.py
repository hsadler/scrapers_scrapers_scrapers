import sys
sys.path.append('..')

import json
from service.scrape import Scrape

scrape_result = Scrape.scrape_hemnet_api()
filepath = '/hemnet_scrape_results.json'
with open(filepath, "w") as f:
    json_string = json.dumps(scrape_result, indent=2, sort_keys=True)
    f.write(json_string)