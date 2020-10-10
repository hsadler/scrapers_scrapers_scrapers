

class SamtryggListing():
    """
    Samtrygg listing model to wrap raw data structure
    """

    ### SAMPLE SAMTRYGG LISTING ###
    # "AmenityDescription": [
    #     11
    # ],
    # "EndRentalDate": null,
    # "FormatedHGPrice": "5 750",
    # "FullAddress": "Gullrands väg 147, 145 64 Norsborg, Sverige",
    # "Furniture": "1",
    # "GeographicPositionLat": 59.2434202,
    # "GeographicPositionLong": 17.8010336,
    # "Headline": "Norsborg - 1rok - tillsv - 5.750kr/mån",
    # "ID": 1607,
    # "ImageUrl": "https://samtryggdata.s3.amazonaws.com/images/286x286/a0c5c54eaadd8fea3d341e171a0263c6.jpg",
    # "NoOfMonthsAvailable": -1,
    # "NoOfRooms": 1,
    # "ObjectType": 7,
    # "PostalCode": "14564",
    # "PostalTown": "Norsborg",
    # "PublishedTs": "/Date(1599802005000)/",
    # "RentalObjectLink": "object/pdekxr0obf5ck6hm0s32/stockholm/botkyrka/gullrands-vag-147/1-rok",
    # "SecretIdentification": "pdEKXR0Obf5cK6hm0s32",
    # "SquareMeters": 30,
    # "StartRentalDate": "/Date(1599868800000)/",
    # "StreetName": "Gullrands väg",
    # "StreetNumber": "147",
    # "ViewingType": "ManualViewing"

    def __init__(
        self,
        raw_listing
    ):
        self.raw_listing = raw_listing


    def get_price(self):
        price_string = self.raw_listing['FormatedHGPrice']
        price_int = int(price_string.replace(' ', ''))
        return price_int


