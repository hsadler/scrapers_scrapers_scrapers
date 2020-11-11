import sys
sys.path.append('..')

import json
import config.scrape_config as scrape_config
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.email_report import EmailReport


# TODO: load processed and unseen processed listings from json files


# email report
EmailReport.email_samtrygg_report(
    sender=secrets_config.email_sender, 
    password=secrets_config.email_sender_password,
    recipients=secrets_config.email_recipients,
    subject=secrets_config.email_subject, 
    new_listings=[], 
    relevant_listings=[]
)

