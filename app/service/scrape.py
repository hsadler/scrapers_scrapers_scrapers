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
        # TODO:
            # 1. call search api (maybe multiple times for different municipalities)
            # 2. collect listing_ids
            # 3. call listing endpoint per listing_id (maybe there's a batch endpoint for this)
            # 4. create listing objects per listing response and collect
            # 5. filter listings
            # 6. return filtered listings
            # NOTE: add config object as arg
        # make calls to blocket search api
        blocket_raw_search_results = cls.scrape_blocket_search(config)
        # TEST: return
        return blocket_raw_search_results

    @classmethod
    def scrape_blocket_search(cls, config):
        agg_results = []
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
            agg_results.append({
                "result": res.json(),
                "post_data": post_data
            })
            time.sleep(1)
        return agg_results

    @classmethod
    def scrape_blocket_listing(cls, config):
        # TODO: impl stub
        pass

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

