import json
import requests
import config.scrape_config as scrape_config


class Scrape():

    
    # SAMTRYGG

    @staticmethod
    def scrape_samtrygg_api(search=None):
        req_url = scrape_config.SAMTRYGG_JSON_API_URL
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

    @staticmethod
    def scrape_blocket():
        # TODO:
            # 1. call search api (maybe multiple times for different municipalities)
            # 2. collect listing_ids
            # 3. call listing endpoint per listing_id (maybe there's a batch endpoint for this)
            # 4. create listing objects per listing response and collect
            # 5. filter listings
            # 6. return filtered listings
            # NOTE: add config object as arg
        # call blocket search api
        blocket_search_post_data = {
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
                "shortName": None,
                "searchString": None,
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
        res = requests.post(
            url=scrape_config.BLOCKET_SEARCH_JSON_API_URL, 
            data=json.dumps(blocket_search_post_data), 
            headers=scrape_config.BLOCKET_JSON_API_HEADERS
        )
        # return json for now
        return res.json()


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

