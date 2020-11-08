

class SamtryggFilterOptions():
    """
    Samtrygg filter options struct
    """


    def __init__(
        self,
        price_range,
        rooms_range,
        square_meters_range,
        city_whitelist,
        pets_allowed,
        washer_dryer_included,
        dishwasher_included
    ):
        self.price_range = price_range
        self.rooms_range = rooms_range
        self.square_meters_range = square_meters_range
        self.city_whitelist = city_whitelist
        self.pets_allowed = pets_allowed
        self.washer_dryer_included = washer_dryer_included
        self.dishwasher_include = dishwasher_included
