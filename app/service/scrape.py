import requests


class Scrape():

    @staticmethod
    def scrape_samtrygg():
        res = requests.get("https://www.samtrygg.se/RentalObject/SearchResult?search=")
        return res.json()
        