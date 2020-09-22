import requests


class Scrape():

    
    @staticmethod
    def scrape_samtrygg_api(search=None):
        req_url = "https://www.samtrygg.se/RentalObject/SearchResult"
        if search is not None:
            req_url += ("?search=" + search)
        res = requests.get(req_url)
        return res.json()

    
    @staticmethod
    def scrape_blocket():
        # NOTE: blocket and qasa use the same api
        pass

    
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
    def scrape_hemnet_api():
        res = requests.get("https://www.hemnet.se/bostader/search/cea7d9ceb034a2be436a133ae6066e468075d8b3")
        return res.json()


    @staticmethod
    def scrape_booli_api():
        res = requests.get("https://www.booli.se/1.json?sort=published&direction=desc&page=1&upcomingSale=")
        return res.json()