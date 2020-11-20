import requests
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
from model.samtrygg_listing import SamtryggListing
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


# test blocket scrape
@app.route('/blocket/relevant/json')
def get_relevant_blocket_results_json():
    url = 'https://api.qasa.se/v1/homes/search'
    headers = {
        "Connection": "keep-alive",
        "Accept": "application/json",
        "X-Brand": "X-Brand",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "https://bostad.blocket.se",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bostad.blocket.se/",
        "Accept-Language": "en-US,en;q=0.9,ko;q=0.8,hr;q=0.7,sv;q=0.6"
    }
    search_string = None
    # search_string = "Stockholm" # testing
    data = {
        "minRoomCount":"3",
        "maxRoomCount":None,
        "maxRent":"24000",
        "currency":None,
        "minRentalLength":"2592000",
        "maxRentalLength":"62208000",
        "minSquareMeters":"50",
        "moveInEarliest":"2020-12-01",
        "moveOutEarliest":None,
        "moveOutLatest":None,
        "sharedHomeOk":False,
        "hasPets":True,
        "requiresWheelchairAccessible":False,
        "furnished":"furnished_both",
        "safeRental":False,
        "homeType":[
            "apartment",
            "terrace_house",
            "loft",
            "duplex"
        ],
        "matchingArea":None,
        "commuteLocation":{
            "shortName": search_string,
            "searchString": search_string,
            "latitude":None,
            "longitude":None,
            "placeId":56,
            "country":"Sweden",
            "countryCode":"SE"
        },
        "areaId":56,
        "helper":{},
        "maxRentSek":"24000",
        "maxRentEur":2400,
        "maxRentCurrency":"SEK",
        "token":"06e64aa419c6d37a1ea6fd4859fc2546",
        "page":1,
        "perPage":50
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    