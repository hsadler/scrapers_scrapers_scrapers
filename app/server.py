import json
from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify
)

import config.scrape_config as scrape_config
import config.samtrygg_processing_1 as samtrygg_processing_config
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.apartment_listing_processing import ApartmentListingProcessing
from model.samtrygg_listing import SamtryggListing

# testing
import config.secrets_config as secrets_config
from service.email_report import EmailReport

# init Flask app instance
app = Flask(
    __name__
)


# ping route (for testing)
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({ 'output': 'hi there' })


# get all Samtrygg results
@app.route('/get_all_samtrygg_results', methods=['GET'])
def get_all_samtrygg_results():
    id_to_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_DATASTORE_FILEPATH
    )
    return jsonify(id_to_listing)


# get processed Samtrygg results
@app.route('/get_processed_samtrygg_results', methods=['GET'])
def get_processed_samtrygg_results():
    # fetch listings from datastore and instantiate listing model objects
    id_to_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_DATASTORE_FILEPATH
    )
    raw_listings = list(id_to_listing.values())
    listings = [SamtryggListing(raw_listing) for raw_listing in raw_listings]
    # process
    processed_listings = ApartmentListingProcessing.process_listings(
        listings=listings, 
        processing_config=samtrygg_processing_config
    )
    # api format
    raw_processed_listings = [
        listing.raw_listing for 
        listing in processed_listings
    ]
    return jsonify({
        'result_count': len(raw_processed_listings),
        'result': raw_processed_listings
    })


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    