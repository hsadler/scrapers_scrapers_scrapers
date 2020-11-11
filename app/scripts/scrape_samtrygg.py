import sys
sys.path.append('..')

import json
import config.scrape_config as scrape_config
from service.scrape import Scrape
from service.apartment_listing_datastore import ApartmentListingDatastore


# scrape api
scrape_result = Scrape.scrape_samtrygg_api()
# format scrape result
id_to_listing = Scrape.format_samtrygg_api_result_for_datastore(
    scrape_result
)
# store to json file
ApartmentListingDatastore.save_samtrygg_data(
    id_to_listing, 
    scrape_config.SAMTRYGG_DATASTORE_FILEPATH
)

