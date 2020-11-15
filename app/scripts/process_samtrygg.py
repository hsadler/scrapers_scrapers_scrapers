import sys
sys.path.append('..')

import json
import config.scrape_config as scrape_config
import config.samtrygg_processing_1 as samtrygg_processing_config
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

# # load previously saved processed listings
# old_processed_id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data( 
#     scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
# )
# # compare new processed listings to old and save ones not seen before to file
# unseen_id_to_listing = {}
# for listing_id, listing in processed_id_to_listing.items():
#     if str(listing_id) not in old_processed_id_to_raw_listing:
#         unseen_id_to_listing[listing_id] = listing

# save processed listings to json file
processed_id_to_raw_listing = {
    key:listing.raw_listing for (key, listing) 
    in processed_id_to_listing.items()
}
ApartmentListingDatastore.save_samtrygg_data(
    processed_id_to_raw_listing, 
    scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
)

# save unseen listings to json file
# unseen_id_to_raw_listing = {
#     key:listing.raw_listing for (key, listing) 
#     in unseen_id_to_listing.items()
# }
# ApartmentListingDatastore.save_samtrygg_data(
#     unseen_id_to_raw_listing, 
#     scrape_config.SAMTRYGG_PROCESSED_UNSEEN_DATASTORE_FILEPATH
# )
