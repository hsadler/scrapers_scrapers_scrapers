
import requests

class ScrapeSamtrygg():

    @staticmethod
    def scrape():
        res = requests.get("https://www.samtrygg.se/RentalObject/SearchResult?search=")
        return res.text