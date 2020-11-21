from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify
)
import config.scrape_config as scrape_config
import config.samtrygg_processing_1 as samtrygg_processing_config
import config.blocket_scrape_config as blocket_scrape_config
from model.samtrygg_listing import SamtryggListing
from service.scrape import Scrape
from service.apartment_listing_datastore import ApartmentListingDatastore
from service.apartment_listing_processing import ApartmentListingProcessing

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


# all samtrygg listings
@app.route('/samtrygg/all')
def get_all_samtrygg_results_page():
    # load listings
    id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_DATASTORE_FILEPATH
    )
    # instantiate objects
    listings = []
    for raw_listing in id_to_raw_listing.values():
        listings.append(SamtryggListing(raw_listing))
    # html format
    html_formatted_listings = []
    for listing in listings:
        html_formatted_listings.append(listing.format_html())
    return '<h1>All Samtrygg Listings:</h1><p>{}</p>'.format(
        '<br>'.join(html_formatted_listings)
    )


# relevant samtrygg listings
@app.route('/samtrygg/relevant')
def get_relevant_samtrygg_results_page():
    # load listings
    id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_PROCESSED_DATASTORE_FILEPATH
    )
    # instantiate objects
    listings = []
    for raw_listing in id_to_raw_listing.values():
        listings.append(SamtryggListing(raw_listing))
    # html format
    html_formatted_listings = []
    for listing in listings:
        html_formatted_listings.append(listing.format_html())
    return '<h1>Relevant Samtrygg Listings:</h1><p>{}</p>'.format(
        '<br>'.join(html_formatted_listings)
    )


# samtrygg listing cities
@app.route('/samtrygg/cities')
def get_samtrygg_cities():
    # load listings
    id_to_raw_listing = ApartmentListingDatastore.load_samtrygg_data(
        scrape_config.SAMTRYGG_DATASTORE_FILEPATH
    )
    # instantiate objects
    listings = []
    for raw_listing in id_to_raw_listing.values():
        listings.append(SamtryggListing(raw_listing))
    # html format
    cities = []
    for listing in listings:
        city = listing.get_city()
        cities.append('<a href="https://www.google.com/maps/search/{} sweden" target="_blank">{}</a>'.format(city, city))
    return '<h1>All Samtrygg Cities:</h1><p>{}</p>'.format(
        '<br>'.join(set(cities))
    )


# relevant blocket json
@app.route('/blocket/relevant/json')
def get_relevant_blocket_results_json():
    scrape_results = Scrape.scrape_blocket(config=blocket_scrape_config)
    return jsonify(scrape_results)


# relevant blocket listings
@app.route('/blocket/relevant')
def get_relevant_blocket_results_page():
    return 'TODO: implement!'


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    