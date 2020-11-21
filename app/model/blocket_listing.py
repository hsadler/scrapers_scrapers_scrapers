

class BlocketListing():
    """
    Blocket listing model to wrap raw data structure

    TODO: finish updating to fit Blocket listing
    """

    PETS_ALLOWED = 10

    ### SAMPLE BLOCKET LISTING ###
    # {
    #   "adPaidAt": null, 
    #   "applicationCount": 0, 
    #   "corporateHome": false, 
    #   "currency": "SEK", 
    #   "declinedCount": 0, 
    #   "duration": {
    #     "end": {
    #       "optimal": "2021-05-31T00:00:00.000Z", 
    #       "ufn": false
    #     }, 
    #     "start": {
    #       "asap": false, 
    #       "optimal": "2020-12-01T00:00:00.000Z"
    #     }
    #   }, 
    #   "external": false, 
    #   "fee": 650, 
    #   "firsthand": false, 
    #   "homeStatus": "normal", 
    #   "homeType": "apartment", 
    #   "id": 208831, 
    #   "inContactCount": 0, 
    #   "landlordApplicationId": null, 
    #   "links": {
    #     "en": "https://en.qasa.se/rent/apartment/maltesholmsvagen-stockholm/208831", 
    #     "fi": "https://en.qasa.se/rent/apartment/maltesholmsvagen-stockholm/208831", 
    #     "fr": "https://en.qasa.se/rent/apartment/maltesholmsvagen-stockholm/208831", 
    #     "sv": "https://qasa.se/hyra/lagenhet/maltesholmsvagen-stockholm/208831"
    #   }, 
    #   "location": {
    #     "country": "Sverige", 
    #     "countryCode": "SE", 
    #     "formattedAddress": "Maltesholmsv\u00e4gen 85, 165 55 H\u00e4sselby, Sverige", 
    #     "latitude": "59.3657526", 
    #     "locality": "Stockholm", 
    #     "longitude": "17.8433099", 
    #     "placeId": "ChIJc-YWyt2fX0YRj8fHh2AS_d4", 
    #     "postalCode": "16555", 
    #     "route": "Maltesholmsv\u00e4gen", 
    #     "shortName": null, 
    #     "streetNumber": "85", 
    #     "sublocality": null
    #   }, 
    #   "matchingCount": 560, 
    #   "origin": null, 
    #   "professional": false, 
    #   "recommendedRent": 13533, 
    #   "rent": 13000, 
    #   "roomCount": 3, 
    #   "safeRental": true, 
    #   "seniorHome": false, 
    #   "shared": false, 
    #   "squareMeters": 70, 
    #   "studentHome": false, 
    #   "uploads": [
    #     {
    #       "fileType": "image", 
    #       "id": 2163767, 
    #       "metadata": {
    #         "order": null, 
    #         "primary": false, 
    #         "rotation": null
    #       }, 
    #       "title": "m bild1.jpg", 
    #       "uploadType": "home_picture", 
    #       "url": "https://qasa-static-prod.s3-eu-west-1.amazonaws.com/img/c19d65bf18a11f58e5a81d4d76ec80bae2fffbeb0edec036ed83638761165332.jpg"
    #     }
    #   ], 
    #   "userUid": "ug59siam"
    # }

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
        return self.PETS_ALLOWED in amenities

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
        # parts.append('AmenityDescription: {}'.format(
        #     ', '.join([str(a) for a in self.raw_listing['AmenityDescription']])
        # ))
        return '<br>'.join(parts) + '<br>'


