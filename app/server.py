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
    id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_DATASTORE_FILEPATH
    )
    result = {
        'result_count': len(id_to_raw_listing),
        'result': id_to_raw_listing
    }
    return jsonify(result)


# get processed Samtrygg results
@app.route('/get_processed_samtrygg_results', methods=['GET'])
def get_processed_samtrygg_results():
    id_to_processed_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
    )
    result = {
        'result_count': len(id_to_processed_raw_listing),
        'result': id_to_processed_raw_listing
    }
    return jsonify(result)


# get unseen Samtrygg results
@app.route('/get_unseen_samtrygg_results', methods=['GET'])
def get_unseen_samtrygg_results():
    id_to_unseen_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_PROCESSED_UNSEEN_DATASTORE_FILEPATH
    )
    result = {
        'result_count': len(id_to_unseen_raw_listing),
        'result': id_to_unseen_raw_listing
    }
    return jsonify(result)


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    