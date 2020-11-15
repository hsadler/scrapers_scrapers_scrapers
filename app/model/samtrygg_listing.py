

class SamtryggListing():
    """
    Samtrygg listing model to wrap raw data structure
    """

    PETS_ALLOWED = 10

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

    # kitchen
    # shower
    # child friendly
    # internet

    def __init__(
        self,
        raw_listing
    ):
        self.raw_listing = raw_listing

    def get_id(self):
        return self.raw_listing['ID']

    def get_title(self):
        return self.raw_listing['Headline']

    def get_web_link(self):
        return 'https://www.samtrygg.se/{}'.format(self.raw_listing['RentalObjectLink'])

    def get_image_url(self):
        return self.raw_listing['ImageUrl']

    def get_price(self):
        price_string = self.raw_listing['FormatedHGPrice']
        price_int = int(price_string.replace(' ', ''))
        return price_int

    def get_rooms(self):
        rooms_int = int(self.raw_listing['NoOfRooms'])
        return rooms_int

    def get_sq_meters(self):
        sq_meters_int = int(self.raw_listing['SquareMeters'])
        return sq_meters_int

    def get_pets_allowed(self):
        amenities = self.raw_listing['AmenityDescription']
        return self.PETS_ALLOWED not in amenities

    def get_city(self):
        city = self.raw_listing['PostalTown']
        return city

    def get_internet_included(self):
        # stub
        pass

    def get_kitchen_included(self):
        # stub
        pass

    def get_shower_included(self):
        # stub
        pass

    def get_is_child_friendly(self):
        # stub
        pass

    def get_api_formatted_parts(self):
        parts = []
        parts.append(self.get_title())
        parts.append('{}'.format(self.get_web_link()))
        parts.append('city: {}'.format(self.get_city()))
        parts.append('price: {}'.format(self.get_price()))
        parts.append('rooms: {}'.format(self.get_rooms()))
        parts.append('sq meters: {}'.format(self.get_sq_meters()))
        return parts

    def format_html(self):
        parts = []
        parts.append('<a href="{}" target="_blank">{}</a>'.format(
            self.get_web_link(),
            self.get_title()
        ))
        parts.append('<img src="{}" style="height: 200px">'.format(
            self.get_image_url()
        ))
        parts.append('city: {}'.format(self.get_city()))
        parts.append('price: {}'.format(self.get_price()))
        parts.append('rooms: {}'.format(self.get_rooms()))
        parts.append('sq meters: {}'.format(self.get_sq_meters()))
        return '<br>'.join(parts) + '<br>'


