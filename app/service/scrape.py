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
        # NOTE: blocket and qasa use the same qasa json api
        pass


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

