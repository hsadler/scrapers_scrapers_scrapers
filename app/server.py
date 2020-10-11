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
from model.samtrygg_listing import SamtryggListing
from model.samtrygg_filter_options import SamtryggFilterOptions
from model.samtrygg_rank_options import SamtryggRankOptions


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
    
    # filter options
    price_min = 10000
    price_max = 20000
    rooms_min = 3
    rooms_max = 5
    sq_meters_min = 70
    sq_meters_max = 110
    location_blacklist = ()
    pets_allowed = True
    washer_dryer_included = True
    dishwasher_included = True
    # instantiate filter options struct
    filter_options = SamtryggFilterOptions(
        price_range=(price_min, price_max),
        rooms_range=(rooms_min, rooms_max),
        square_meters_range=(sq_meters_min, sq_meters_max),
        location_blacklist=location_blacklist,
        pets_allowed=pets_allowed,
        washer_dryer_included=washer_dryer_included,
        dishwasher_included=dishwasher_included
    )
    # filter the listings
    filtered_listings = ApartmentListingProcessing.filter_samtrygg_listings(
        listings,
        filter_options
    )
    
    # rank options
    listing_freshness_weight = 100
    price_per_square_meter_weight = 100
    optimal_room_amount_and_weight = (4, 100)
    favorite_locations_and_weight = ([], 100)
    is_furninshed_and_weight = (None, 100)
    # instantiate rank options struct
    rank_options = SamtryggRankOptions(
        listing_freshness_weight=listing_freshness_weight,
        price_per_square_meter_weight=price_per_square_meter_weight,
        optimal_room_amount_and_weight=optimal_room_amount_and_weight,
        favorite_locations_and_weight=favorite_locations_and_weight,
        is_furninshed_and_weight=is_furninshed_and_weight
    )
    # rank the listings
    ranked_listings = ApartmentListingProcessing.rank_samtrygg_listings(
        filtered_listings,
        rank_options
    )

    processed_raw_listings = [listing.raw_listing for listing in ranked_listings]
    return jsonify(processed_raw_listings)


# run the app if executed as main file from python interpreter
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    