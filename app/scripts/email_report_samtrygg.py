import sys
sys.path.append('..')

import json
import config.secrets_config as secrets_config
import config.scrape_config as scrape_config
from model.samtrygg_listing import SamtryggListing
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.email_report import EmailReport


print('==================> emailing samtrygg results...')

# load processed and unseen listings
unseen_id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data( 
    scrape_config.SAMTRYGG_PROCESSED_UNSEEN_DATASTORE_FILEPATH
)
processed_id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data( 
    scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
)
# convert to objects
new_listings = []
relevant_listings = []
for raw_listing in unseen_id_to_raw_listing.values():
    new_listings.append(SamtryggListing(raw_listing))
for raw_listing in processed_id_to_raw_listing.values():
    relevant_listings.append(SamtryggListing(raw_listing))

# email report
EmailReport.email_samtrygg_report(
    sender=secrets_config.email_sender, 
    password=secrets_config.email_sender_password,
    recipients=secrets_config.email_recipients,
    subject=secrets_config.email_subject, 
    new_listings=new_listings, 
    relevant_listings=relevant_listings
)

