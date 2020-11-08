import json
from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify
)

import config.samtrygg_processing_1 as samtrygg_processing_config
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.apartment_listing_processing import ApartmentListingProcessing
from model.samtrygg_listing import SamtryggListing


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
    id_to_listing = ApartmentListingDatastore.get_samtrygg_data()
    return jsonify(id_to_listing)


# get processed Samtrygg results
@app.route('/get_processed_samtrygg_results', methods=['GET'])
def get_processed_samtrygg_results():
    # fetch listings from datastore and instantiate listing model objects
    id_to_listing = ApartmentListingDatastore.get_samtrygg_data()
    raw_listings = list(id_to_listing.values())
    listings = [SamtryggListing(raw_listing) for raw_listing in raw_listings]
    # process
    processed_listings = ApartmentListingProcessing.get_processed_listings(
        listings=listings, 
        processing_config=samtrygg_processing_config
    )
    # api format
    raw_processed_listings = [
        listing.raw_listing for 
        listing in processed_listings
    ]
    return jsonify(raw_processed_listings)


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    