import json
from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify
)
import config.scrape_config as scrape_config
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.apartment_listing_processing import ApartmentListingProcessing


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
    listings = list(id_to_listing.values())
    return jsonify(listings)


# get processed Samtrygg results
@app.route('/get_processed_samtrygg_results', methods=['GET'])
def get_processed_samtrygg_results():
    id_to_listing = ApartmentListingDatastore.get_samtrygg_data()
    listings = list(id_to_listing.values())
    filtered_listings = ApartmentListingProcessing.filter_samtrygg_listings(
        listings
    )
    ranked_listings = ApartmentListingProcessing.rank_samtrygg_listings(
        filtered_listings
    )
    return jsonify(ranked_listings)


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    