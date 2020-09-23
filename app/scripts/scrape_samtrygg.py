import sys
sys.path.append('..')

import json
import config.scrape_config as scrape_config
from service.scrape import Scrape

# scrape api
search_term = ''
scrape_result = Scrape.scrape_samtrygg_api(search_term)
# format scrape result
id_to_listing = Scrape.format_samtrygg_api_result_for_datastore(
    scrape_result
)
# store to json file
with open(scrape_config.SAMTRYGG_DATASTORE_FILEPATH, "w") as f:
    json_string = json.dumps(id_to_listing, indent=2, sort_keys=True)
    f.write(json_string)