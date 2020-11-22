import json
import requests
import time


class Scrape():

    
    # SAMTRYGG

    @staticmethod
    def scrape_samtrygg_api(config, search=None):
        req_url = config.SAMTRYGG_JSON_API_URL
        if search is not None:
            req_url += ('?search=' + search)
        res = requests.get(req_url)
        return res.json()

    @staticmethod
    def format_samtrygg_api_result_for_datastore(samtrygg_api_result):
        listings = samtrygg_api_result['SearchResult']
        id_to_listing = {}
        for listing in listings:
            id_to_listing[listing['ID']] = listing
        return id_to_listing


    # BLOCKET

    @classmethod
    def scrape_blocket(cls, config):
        # make calls to blocket search api
        id_to_raw_listing = cls.scrape_blocket_search(config)
        # return raw listings
        return id_to_raw_listing.values()

    @classmethod
    def scrape_blocket_search(cls, config):
        search_results = []
        # make a call for each search area defined by the config
        for search_area in config.SEARCH_AREAS:
            post_data = cls.compose_blocket_post_data_for_search(
                config,
                search_area
            )
            res = requests.post(
                url=config.SEARCH_JSON_API_URL, 
                data=json.dumps(post_data), 
                headers=config.JSON_API_HEADERS
            )
            search_results.append(res.json())
            time.sleep(1)
        # dedupe the results by listing_id
        id_to_raw_listing = {}
        for sr in search_results:
            for l in sr['filterHomes']:
                id_to_raw_listing[l['id']] = l
        return id_to_raw_listing

    @classmethod
    def compose_blocket_post_data_for_search(cls, config, search_area):
        blocket_search_post_data = {
            "minRoomCount": config.SEARCH_PARAMS['min_room_count'],
            "maxRoomCount": config.SEARCH_PARAMS['max_room_count'],
            "maxRent": config.SEARCH_PARAMS['max_rent'],
            "currency":None,
            "minRentalLength": config.SEARCH_PARAMS['min_rental_length'],
            "maxRentalLength": config.SEARCH_PARAMS['max_rental_length'],
            "minSquareMeters": config.SEARCH_PARAMS['min_square_meters'],
            "moveInEarliest": config.SEARCH_PARAMS['move_in_earliest'],
            "moveOutEarliest": config.SEARCH_PARAMS['move_out_earliest'],
            "moveOutLatest":None,
            "sharedHomeOk":False,
            "hasPets": config.SEARCH_PARAMS['has_pets'],
            "requiresWheelchairAccessible":False,
            "furnished":"furnished_both",
            "safeRental":False,
            "homeType": config.SEARCH_PARAMS['home_type'],
            "matchingArea": search_area['matching_area'],
            "commuteLocation": search_area['commute_location'],
            "areaId":56,
            "helper":{},
            "maxRentSek":"24000",
            "maxRentEur":2400,
            "maxRentCurrency":"SEK",
            "token":"06e64aa419c6d37a1ea6fd4859fc2546",
            "page":1,
            "perPage":50
        }
        return blocket_search_post_data

    @classmethod
    def html_format_from_raw_blocket_listing(cls, raw_listing):
        l = raw_listing
        parts = []
        parts.append('<a href="{}" target="_blank">{}</a>'.format(
            l['links']['en'],
            l['location']['formattedAddress']
        ))
        parts.append('<img src="{}" style="height: 200px">'.format(
            l['uploads'][0]['url']
        ))
        parts.append('city: {}'.format(l['location']['locality']))
        parts.append('price: {}'.format(l['rent']))
        parts.append('rooms: {}'.format(l['roomCount']))
        parts.append('sq meters: {}'.format(l['squareMeters']))
        return '<br>'.join(parts) + '<br>'


    # QASA
    
    @staticmethod
    def scrape_qasa_api():
        # params:
            # furnished: null
            # hasPets: null
            # maxRent: null
            # maxRentCurrency: "SEK"
            # maxRentalLength: null
            # maxRoomCount: null
            # minRentalLength: null
            # minRoomCount: null
            # minSquareMeters: null
            # moveInEarliest: null
            # moveOutEarliest: null
            # moveOutLatest: null
            # page: "2"
            # perPage: 50
        res = requests.get("https://api.qasa.se/v1/homes/search")
        return res.json()

    @staticmethod
    def format_qasa_api_result_for_datastore(qasa_api_result):
        # stub
        pass
        

    # HEMNET

    @staticmethod
    def scrape_hemnet_api():
        res = requests.get("https://www.hemnet.se/bostader/search/cea7d9ceb034a2be436a133ae6066e468075d8b3")
        return res.json()

    @staticmethod
    def format_hemnet_api_result_for_datastore(hemnet_api_result):
        # stub
        pass


    # BOOLI

    @staticmethod
    def scrape_booli_api():
        res = requests.get("https://www.booli.se/1.json?sort=published&direction=desc&page=1&upcomingSale=")
        return res.json()

    @staticmethod
    def format_booli_api_result_for_datastore(booli_api_result):
        # stub
        pass

