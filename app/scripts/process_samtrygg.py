import sys
sys.path.append('..')

import json
import config.scrape_config as scrape_config
import config.samtrygg_processing as samtrygg_processing_config
from model.samtrygg_listing import SamtryggListing
from service.apartment_listing_processing import ApartmentListingProcessing
from service.apartment_listing_datastore import ApartmentListingDatastore


print('==================> processing samtrygg results...')

# load listings from datastore and instantiate listing model objects
id_to_listing = ApartmentListingDatastore.load_samtrygg_data(
    scrape_config.SAMTRYGG_DATASTORE_FILEPATH
)
raw_listings = list(id_to_listing.values())
listings = [SamtryggListing(raw_listing) for raw_listing in raw_listings]
# process listings
processed_listings = ApartmentListingProcessing.process_listings(
    listings=listings, 
    processing_config=samtrygg_processing_config
)
# format processed listings structure
processed_id_to_listing = {}
for listing in processed_listings:
    processed_id_to_listing[listing.get_id()] = listing

# save processed listings to json file
processed_id_to_raw_listing = {
    key:listing.raw_listing for (key, listing) 
    in processed_id_to_listing.items()
}
ApartmentListingDatastore.save_samtrygg_data(
    processed_id_to_raw_listing, 
    scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
)
